# FrontierForge — Frontier Computation Workbench

**Version 1.0 | CPU-only | Pure Python reference implementations**

FrontierForge is a separate experimental workspace for exploring computational paradigms that are not yet routine in mainstream application engineering. It turns three ideas into runnable, inspectable CPU simulations and shows how their outputs can inform real product decisions:

1. **Hybrid quantum-classical optimization** — QAOA-style statevector simulation for small product architecture/resource-allocation graphs.
2. **Neuromorphic/event-based computing** — leaky-integrate-and-fire (LIF) neurons and event-burst detection for sparse sensor/telemetry streams.
3. **Probabilistic computing for engineering decisions** — Bayesian Beta-Binomial inference to quantify uncertainty in test failure rates and release risk.

This is not a quantum computer, neuromorphic chip, or production reliability certification. All V1 engines execute locally on a conventional CPU. The quantum simulator is exponential in qubit count and intentionally limited to 10 qubits.

## Quick start

```bash
python3 --version                 # Python 3.10+
./setup.sh
.venv/bin/python -m frontierforge.cli quantum-demo
.venv/bin/python -m frontierforge.cli neuro-demo
.venv/bin/python -m frontierforge.cli risk --failures 3 --trials 40
.venv/bin/python -m unittest discover -s tests -v
```

No external Python packages are required. Run from this directory. Windows users can use `py -m venv .venv` and `.venv\\Scripts\\python.exe -m frontierforge.cli ...`.

## What each engine demonstrates

### Quantum optimization

`quantum-demo` builds a small MaxCut graph, prepares a uniform state, applies a p=1 QAOA cost unitary and mixer, and computes the exact statevector expectation. A deterministic angle grid searches for a good parameter pair. This is a small, auditable simulator—not evidence of quantum advantage. Increase `--qubits` cautiously; state memory grows as `2**n`.

### Neuromorphic/event computation

`neuro-demo` feeds a sparse event stream into a LIF neuron and a sliding-window event-burst detector. This demonstrates temporal integration and event-driven processing without requiring dense frame-by-frame inference or neuromorphic hardware.

### Bayesian product-risk computation

`risk` updates a Beta prior with observed pass/fail evidence, then numerically integrates the posterior tail probability that the true failure rate exceeds a specified threshold. It makes uncertainty explicit instead of treating a small test sample as certainty.

## Suggested next steps

- Add Qiskit Aer / PennyLane / CUDA-Q adapters as optional backends; preserve CPU reference results for regression checks.
- Add Lava/NIR adapters for interoperable spiking-network experiments.
- Add data ingestion from test reports, telemetry and CI systems, with provenance and schema validation.
- Add experiment tracking: inputs, seeds, algorithm version, runtime, output, confidence and reproducibility metadata.
- Benchmark classical baselines before making any performance or advantage claims.

See `docs/` for architecture, use cases, research notes and roadmap.
