"""Minimal leaky-integrate-and-fire event-processing simulator."""

def lif_run(events, threshold=1.0, decay=0.85, refractory_steps=1):
    """events: list of non-negative scalar input currents per time step."""
    if not 0 < decay <= 1 or threshold <= 0: raise ValueError('invalid neuron parameters')
    v=0.0; refractory=0; spikes=[]; trace=[]
    for t,current in enumerate(events):
        if current < 0: raise ValueError('events/current must be non-negative')
        if refractory:
            refractory-=1; v=0.0
        else:
            v=v*decay+float(current)
            if v>=threshold:
                spikes.append(t); v=0.0; refractory=refractory_steps
        trace.append(round(v,6))
    return {'engine':'lif_event_simulator_cpu','steps':len(events),'spike_times':spikes,
            'spike_count':len(spikes),'membrane_trace':trace,
            'note':'Software simulation of a simple spiking neuron; no neuromorphic chip required.'}

def detect_bursts(events, window=5, threshold=3):
    """Detect high-activity windows using a tiny event-count SNN-inspired front end."""
    if window < 1 or threshold < 1: raise ValueError('window and threshold must be positive')
    hits=[]
    for start in range(max(0,len(events)-window+1)):
        count=sum(1 for x in events[start:start+window] if x>0)
        if count>=threshold: hits.append({'start':start,'end':start+window-1,'events':count})
    return {'engine':'event_burst_detector_cpu','windows':len(hits),'bursts':hits,
            'note':'Illustrative event-based detector; tune thresholds on representative product data.'}
