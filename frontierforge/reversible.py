"""Reversible-logic demonstrator: self-inverse gates, a reversible full adder,
and Landauer-limit accounting.

All supported gates are their own inverses, so any circuit is reversed by
replaying its gates in reverse order.  The full adder uses one clean ancilla
and returns sum/carry while leaving two garbage bits, so no information is
erased during the computation itself.
"""
from __future__ import annotations
import math

BOLTZMANN_J_K = 1.380649e-23
DEFAULT_TEMPERATURE_K = 300.15


def _validate(circuit, wires):
    for gate in circuit:
        name, targets = gate[0], tuple(gate[1:])
        if name == 'X':
            valid = len(targets) == 1
        elif name == 'CNOT':
            valid = len(targets) == 2 and targets[0] != targets[1]
        elif name == 'SWAP':
            valid = len(targets) == 2 and targets[0] != targets[1]
        elif name == 'TOFFOLI':
            valid = len(targets) == 3 and len(set(targets)) == 3
        elif name == 'FREDKIN':
            valid = len(targets) == 3 and len(set(targets)) == 3
        else:
            raise ValueError(f'unknown gate {name!r}')
        if not valid:
            raise ValueError(f'invalid targets for {name}: {targets}')
        if any(not 0 <= t < wires for t in targets):
            raise ValueError('gate target outside wire range')


def apply_gate(bits, gate):
    name, targets = gate[0], tuple(gate[1:])
    out = list(bits)
    if name == 'X':
        out[targets[0]] ^= 1
    elif name == 'CNOT':
        if out[targets[0]]:
            out[targets[1]] ^= 1
    elif name == 'SWAP':
        out[targets[0]], out[targets[1]] = out[targets[1]], out[targets[0]]
    elif name == 'TOFFOLI':
        if out[targets[0]] and out[targets[1]]:
            out[targets[2]] ^= 1
    elif name == 'FREDKIN':
        if out[targets[0]]:
            out[targets[1]], out[targets[2]] = out[targets[2]], out[targets[1]]
    else:
        raise ValueError(f'unknown gate {name!r}')
    return out


def run_reversible(bits, circuit, wires=None):
    """Apply a circuit to a bit vector."""
    n = len(bits) if wires is None else wires
    _validate(circuit, n)
    if len(bits) != n:
        raise ValueError('bit vector length does not match wire count')
    state = list(bits)
    for gate in circuit:
        state = apply_gate(state, gate)
    return state


def inverse_circuit(circuit):
    """Reverse a circuit; valid because every supported gate is self-inverse."""
    return list(reversed(circuit))


def is_bijective(circuit, wires):
    """Exhaustively check that the circuit is a permutation of the state space."""
    if not 2 <= wires <= 12:
        raise ValueError('bijectivity enumeration supports 2..12 wires')
    _validate(circuit, wires)
    seen = set()
    for value in range(1 << wires):
        bits = [(value >> q) & 1 for q in range(wires)]
        out = run_reversible(bits, circuit, wires)
        key = sum(bit << q for q, bit in enumerate(out))
        if key in seen:
            return False
        seen.add(key)
    return len(seen) == (1 << wires)


def circuit_depth(circuit, wires):
    """Number of parallel time slices needed (greedy ASAP scheduling)."""
    _validate(circuit, wires)
    wire_time = [0] * wires
    depth = 0
    for gate in circuit:
        targets = tuple(gate[1:])
        start = max(wire_time[t] for t in targets)
        end = start + 1
        for t in targets:
            wire_time[t] = end
        depth = max(depth, end)
    return depth


def gate_counts(circuit):
    counts = {}
    for gate in circuit:
        counts[gate[0]] = counts.get(gate[0], 0) + 1
    return counts


def full_adder_circuit():
    """Reversible full adder: wires [a, b, cin, carry_ancilla(0)].

    Final mapping: wire 2 holds sum, wire 3 holds carry-out; wires 0 and 1 are
    preserved/garbage (a and a XOR b).  Uses 2 Toffoli + 2 CNOT.
    """
    return [
        ('TOFFOLI', 0, 1, 3),
        ('CNOT', 0, 1),
        ('TOFFOLI', 1, 2, 3),
        ('CNOT', 1, 2),
    ]


def landauer_bound(temperature_k=DEFAULT_TEMPERATURE_K):
    """Landauer energy per irreversibly erased bit: k_B * T * ln(2)."""
    if temperature_k <= 0:
        raise ValueError('temperature must be positive')
    return BOLTZMANN_J_K * temperature_k * math.log(2)


def analyze_full_adder(temperature_k=DEFAULT_TEMPERATURE_K):
    circuit = full_adder_circuit()
    wires = 4
    truth_table = []
    passed = True
    for value in range(8):
        a, b, cin = (value >> 2) & 1, (value >> 1) & 1, value & 1
        state = run_reversible([a, b, cin, 0], circuit, wires)
        total_sum, carry = state[2], state[3]
        expected_sum = a ^ b ^ cin
        expected_carry = (a & b) | (cin & (a ^ b))
        ok = total_sum == expected_sum and carry == expected_carry
        passed = passed and ok
        truth_table.append({
            'a': a, 'b': b, 'cin': cin,
            'sum': total_sum, 'carry': carry,
            'expected_sum': expected_sum, 'expected_carry': expected_carry,
            'pass': ok,
        })

    roundtrip_ok = True
    for value in range(1 << wires):
        bits = [(value >> q) & 1 for q in range(wires)]
        restored = run_reversible(run_reversible(bits, circuit, wires),
                                  inverse_circuit(circuit), wires)
        roundtrip_ok = roundtrip_ok and restored == bits

    per_bit = landauer_bound(temperature_k)
    return {
        'engine': 'reversible_logic_cpu',
        'wires': wires,
        'gate_counts': gate_counts(circuit),
        'gate_count': len(circuit),
        'circuit_depth': circuit_depth(circuit, wires),
        'ancilla_bits': 1,
        'garbage_bits': 2,
        'truth_table': truth_table,
        'truth_table_pass': passed,
        'bijective': is_bijective(circuit, wires),
        'inverse_roundtrip_pass': roundtrip_ok,
        'landauer': {
            'temperature_kelvin': temperature_k,
            'energy_per_erased_bit_joules': per_bit,
            'irreversible_adder_min_bits_erased': 1,
            'irreversible_adder_min_energy_joules': per_bit,
            'reversible_adder_min_energy_joules': 0.0,
        },
        'note': ('Logical reversibility is exact here; Landauer values are theoretical '
                 'lower bounds for bit erasure, not measured device energy.'),
    }
