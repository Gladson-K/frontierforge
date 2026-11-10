"""Small pure-Python state-vector and QAOA MaxCut demonstrator.

Educational CPU simulator. Exponential memory/time: keep graphs to <= 10 qubits.
"""
from __future__ import annotations
import cmath, math

Complex = complex

def _apply_single(state, n, q, matrix):
    out = state[:]
    bit = 1 << q
    for base in range(len(state)):
        if base & bit == 0:
            j = base | bit
            a, b = state[base], state[j]
            out[base] = matrix[0][0]*a + matrix[0][1]*b
            out[j] = matrix[1][0]*a + matrix[1][1]*b
    return out

def _h(state, n, q):
    s = 1/math.sqrt(2)
    return _apply_single(state,n,q,((s,s),(s,-s)))

def _rx(state,n,q,theta):
    c,s=math.cos(theta/2),-1j*math.sin(theta/2)
    return _apply_single(state,n,q,((c,s),(s,c)))

def _phase_cut(state, edges, gamma):
    out=state[:]
    for idx,amp in enumerate(state):
        cut=sum(((idx>>u)&1) != ((idx>>v)&1) for u,v in edges)
        out[idx] = amp*cmath.exp(-1j*gamma*cut)
    return out

def _expectation(state, edges):
    return sum(abs(a)**2 * sum(((i>>u)&1) != ((i>>v)&1) for u,v in edges)
               for i,a in enumerate(state))

def qaoa_maxcut(n, edges, p=1, angle_steps=9):
    """Grid-search QAOA angles on a statevector; returns best bitstring and score."""
    if not 2 <= n <= 10: raise ValueError('QAOA demo supports 2..10 qubits')
    if not edges or any(u==v or min(u,v)<0 or max(u,v)>=n for u,v in edges):
        raise ValueError('edges must contain valid (u, v) pairs')
    if p != 1: raise ValueError('V1 implements p=1 only')
    best=(-1.0,None,None)
    # Deterministic coarse angle grid; no random seed or external quantum service.
    for gi in range(angle_steps):
        gamma=(gi+0.5)*math.pi/angle_steps
        for bi in range(angle_steps):
            beta=(bi+0.5)*math.pi/angle_steps
            state=[1/math.sqrt(2**n)]*(2**n)
            state=_phase_cut(state,edges,gamma)
            for q in range(n): state=_rx(state,n,q,2*beta)
            exp=_expectation(state,edges)
            if exp>best[0]: best=(exp,gamma,beta)
    exp,gamma,beta=best
    state=[1/math.sqrt(2**n)]*(2**n)
    state=_phase_cut(state,edges,gamma)
    for q in range(n): state=_rx(state,n,q,2*beta)
    probs=[abs(a)**2 for a in state]
    top=max(range(len(probs)),key=probs.__getitem__)
    bits=format(top, f'0{n}b')[::-1]
    cut=sum(bits[u]!=bits[v] for u,v in edges)
    return {'engine':'qaoa_statevector_cpu','qubits':n,'edges':[list(e) for e in edges],
            'p':1,'gamma':gamma,'beta':beta,'expected_cut':exp,
            'most_likely_bitstring_q0_first':bits,'sampled_bitstring_cut':cut,
            'statevector_dimension':2**n,
            'note':'Exact statevector simulation, not execution on quantum hardware.'}
