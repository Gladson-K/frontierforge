# Roadmap

- **V1 (included):** pure-Python CPU reference kernels, CLI, synthetic demos and unit tests.
- **V1.1:** experiment manifests (YAML/JSON), seeded benchmark harness, exact classical MaxCut baseline, parameter sweeps and CSV/JSON export.
- **V2:** optional Qiskit/PennyLane/CUDA-Q adapters; optional Lava/NIR adapter; posterior predictive checks and richer reliability models.
- **V3:** product integrations (CI test results, telemetry, issue tracker), provenance, artifact hashing, experiment comparison and reproducible runs.
- **V4:** multi-engine workflow orchestration and hardware/cloud execution adapters where access is available.

Release gates: numerical correctness tests; deterministic replay; resource limits; baseline comparisons; clear labeling of simulated versus physical execution; no quantum/energy/accuracy advantage claims without measured evidence.
