# FrontierForge — Frontier Computation Workbench

**Version 2.0.0 | CPU-only | Pure Python reference implementations**

FrontierForge is a separate experimental workspace for exploring computational paradigms that are not yet routine in mainstream application engineering. V1 covered quantum-classical optimization, neuromorphic event streams and Bayesian release risk. V2 adds four CPU simulations: coherent photonic meshes, cellular automata, reversible logic and reservoir computing.

All engines are local, deterministic where seeded, and produce JSON-serializable dictionaries. This is not quantum hardware, optical hardware, a neuromorphic chip, a validated reliability model, or evidence of an advantage. The quantum simulator remains limited to 10 qubits.

## Quick start

```bash
python3 --version                 # Python 3.10+
./setup.sh
.venv/bin/python -m frontierforge.cli quantum-demo
.venv/bin/python -m frontierforge.cli neuro-demo
.venv/bin/python -m frontierforge.cli risk --failures 3 --trials 40
.venv/bin/python -m frontierforge.cli photonic-demo
.venv/bin/python -m frontierforge.cli ca-demo
.venv/bin/python -m frontierforge.cli reversible-demo
.venv/bin/python -m frontierforge.cli reservoir-demo
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python tests/run_and_report.py --docker
```

No external Python packages are required. Run from this directory. Windows users can use `py -m venv .venv` and `.venv\\Scripts\\python.exe -m frontierforge.cli ...`.

## Engines

### V1 — included unchanged

- `quantum-demo`: p=1 QAOA MaxCut statevector simulation with deterministic angle search.
- `neuro-demo`: leaky-integrate-and-fire neuron and sliding-window burst detection.
- `risk`: Beta-Binomial posterior mean, spread and tail probability for release risk.

### V2 — new in 2.0.0

- `photonic-demo`: Clements-style MZI mesh propagating complex amplitudes; a coherent classifier where intensity-only input features cannot separate the synthetic classes. Energy figures are labelled single-photon heuristics.
- `ca-demo`: elementary 1D rules, 2D majority and Game of Life; a local-only load-consensus demo compared with a global-mean threshold baseline that assumes centralised readings.
- `reversible-demo`: self-inverse gate circuits, a four-gate reversible full adder, truth-table and bijectivity checks, and a Landauer lower bound for irreversible erasure.
- `reservoir-demo`: seeded echo-state network with pure-Python Cholesky ridge readout, compared against AR(5) and persistence on a synthetic maintenance trace.

## Testing and verification

- Focused engine tests: `tests/test_photonic.py`, `tests/test_cellular.py`, `tests/test_reversible.py`, `tests/test_reservoir.py`.
- Full suite: `python -m unittest discover -s tests -v`.
- `tests/run_and_report.py` runs local tests, all CLI demos and optionally the eight Docker pipelines, then writes `docs/TEST-RESULTS.md` with full logs for every command and per-testcase statuses, including failures.
- Docker has one image per use case plus a test image; see `docs/DOCKER.md`.

## Governance and claims

Risk tier B: advisory experiments only. A named human reviews changes before merge; AI assistance and verification are recorded in `AI-USE.md` and the change description. Synthetic fixtures only; no personal, health, secret or restricted data is used. No quantum, photonic, energy, accuracy or safety advantage is claimed without measured evidence and review.

See `docs/` for architecture, use cases, research notes, references, Docker pipelines, roadmap and recorded test results.
