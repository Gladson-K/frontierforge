# Roadmap

- **V1 (delivered):** pure-Python CPU reference kernels — QAOA statevector, LIF/event bursts, Beta-Binomial risk — with CLI, synthetic demos, unit tests and an initial tag `v1.0.0`.
- **V2 (delivered in `2.0.0`):** four additional engines — coherent photonic MZI mesh, cellular automata, reversible circuits with Landauer accounting, and reservoir computing — with per-engine tests, per-use-case Docker images, example outputs and full logged testcase results.
- **V2.1 (next hardening):** experiment manifests with inputs/seeds/runtime/output hashes, parameter sweeps and JSON/CSV export; optional backend adapters that preserve CPU reference regression checks.
- **V3:** multi-engine workflow orchestration, data ingestion from test reports/telemetry/CI, provenance, artefact hashing and reproducible experiment comparison. Optional Qiskit/PennyLane/CUDA-Q, Lava/NIR and digital-twin adapters remain separate from the reference core.
- **V4:** hardware/cloud execution adapters only where access, safety review and measured baselines exist.

Release gates: numerical correctness tests, deterministic replay, resource limits, baseline comparisons, clear labeling of simulated versus physical execution, AI-use disclosure, Tier B review (tests, dependency/SBOM check, security and privacy review), and no quantum/photonic/energy/accuracy advantage claims without measured evidence.
