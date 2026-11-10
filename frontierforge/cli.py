import argparse, json
from .quantum import qaoa_maxcut
from .neuromorphic import lif_run, detect_bursts
from .bayes import failure_risk

def main():
    p=argparse.ArgumentParser(prog='frontierforge',description='Frontier computation workbench (CPU-only V1)')
    sub=p.add_subparsers(dest='cmd',required=True)
    q=sub.add_parser('quantum-demo'); q.add_argument('--qubits',type=int,default=4); q.add_argument('--steps',type=int,default=9)
    n=sub.add_parser('neuro-demo')
    b=sub.add_parser('risk'); b.add_argument('--failures',type=int,default=3); b.add_argument('--trials',type=int,default=40); b.add_argument('--threshold',type=float,default=.1)
    args=p.parse_args()
    if args.cmd=='quantum-demo':
        edges=[(0,1),(1,2),(2,3),(3,0),(0,2)] if args.qubits==4 else [(i,(i+1)%args.qubits) for i in range(args.qubits)]
        result=qaoa_maxcut(args.qubits,edges,angle_steps=args.steps)
    elif args.cmd=='neuro-demo':
        stream=[0,0,.2,.3,.9,0,0,1.2,0,.1,.8,.7,.9,0,0,0,1.3]
        result={'lif':lif_run(stream,threshold=1.0),'burst_analysis':detect_bursts(stream,window=4,threshold=3)}
    else: result=failure_risk(args.failures,args.trials,risk_threshold=args.threshold)
    print(json.dumps(result,indent=2))
if __name__=='__main__': main()
