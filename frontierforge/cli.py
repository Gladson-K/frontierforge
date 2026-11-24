import argparse, json
from .quantum import qaoa_maxcut
from .neuromorphic import lif_run, detect_bursts
from .bayes import failure_risk
from .photonic import photonic_classifier
from .cellular import load_consensus
from .reversible import analyze_full_adder
from .reservoir import reservoir_forecast

def main():
    p=argparse.ArgumentParser(prog='frontierforge',description='Frontier computation workbench (CPU-only V2)')
    sub=p.add_subparsers(dest='cmd',required=True)
    q=sub.add_parser('quantum-demo'); q.add_argument('--qubits',type=int,default=4); q.add_argument('--steps',type=int,default=9)
    n=sub.add_parser('neuro-demo')
    b=sub.add_parser('risk'); b.add_argument('--failures',type=int,default=3); b.add_argument('--trials',type=int,default=40); b.add_argument('--threshold',type=float,default=.1)
    ph=sub.add_parser('photonic-demo'); ph.add_argument('--ports',type=int,default=4); ph.add_argument('--samples',type=int,default=30); ph.add_argument('--seed',type=int,default=7); ph.add_argument('--sweeps',type=int,default=6)
    ca=sub.add_parser('ca-demo'); ca.add_argument('--size',type=int,default=12); ca.add_argument('--steps',type=int,default=30); ca.add_argument('--noise',type=float,default=.15); ca.add_argument('--seed',type=int,default=11)
    sub.add_parser('reversible-demo')
    rc=sub.add_parser('reservoir-demo'); rc.add_argument('--length',type=int,default=300); rc.add_argument('--units',type=int,default=40); rc.add_argument('--seed',type=int,default=3)
    args=p.parse_args()
    if args.cmd=='quantum-demo':
        edges=[(0,1),(1,2),(2,3),(3,0),(0,2)] if args.qubits==4 else [(i,(i+1)%args.qubits) for i in range(args.qubits)]
        result=qaoa_maxcut(args.qubits,edges,angle_steps=args.steps)
    elif args.cmd=='neuro-demo':
        stream=[0,0,.2,.3,.9,0,0,1.2,0,.1,.8,.7,.9,0,0,0,1.3]
        result={'lif':lif_run(stream,threshold=1.0),'burst_analysis':detect_bursts(stream,window=4,threshold=3)}
    elif args.cmd=='risk': result=failure_risk(args.failures,args.trials,risk_threshold=args.threshold)
    elif args.cmd=='photonic-demo': result=photonic_classifier(args.ports,args.samples,args.seed,args.sweeps)
    elif args.cmd=='ca-demo': result=load_consensus(args.size,args.steps,args.noise,args.seed)
    elif args.cmd=='reversible-demo': result=analyze_full_adder()
    else: result=reservoir_forecast(args.length,args.units,args.seed)
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
