"""Beta-Binomial uncertainty engine for engineering test evidence."""
import math

def _beta_pdf(x,a,b):
    if x<=0 or x>=1: return 0.0
    log_norm=math.lgamma(a+b)-math.lgamma(a)-math.lgamma(b)
    return math.exp(log_norm+(a-1)*math.log(x)+(b-1)*math.log1p(-x))

def failure_risk(failures, trials, prior_a=1.0, prior_b=9.0, risk_threshold=0.10, grid=4000):
    """Posterior failure probability and P(true failure rate > risk_threshold)."""
    if trials<0 or failures<0 or failures>trials: raise ValueError('require 0 <= failures <= trials')
    if prior_a<=0 or prior_b<=0 or not 0<risk_threshold<1: raise ValueError('invalid prior/threshold')
    a=prior_a+failures; b=prior_b+trials-failures
    mean=a/(a+b); variance=a*b/((a+b)**2*(a+b+1))
    # Midpoint integration of posterior density on [threshold, 1].
    lo=risk_threshold; dx=(1-lo)/grid
    tail=sum(_beta_pdf(lo+(i+0.5)*dx,a,b) for i in range(grid))*dx
    return {'engine':'beta_binomial_risk_cpu','observed_failures':failures,'trials':trials,
            'posterior_alpha':a,'posterior_beta':b,'posterior_mean_failure_rate':mean,
            'posterior_stddev':math.sqrt(variance),'risk_threshold':risk_threshold,
            'probability_true_failure_rate_exceeds_threshold':min(1.0,max(0.0,tail)),
            'decision':'review' if tail>=0.5 else 'within_threshold',
            'note':'Bayesian estimate from test evidence; not a guarantee of future field reliability.'}
