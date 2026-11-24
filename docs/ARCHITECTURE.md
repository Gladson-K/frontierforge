# Architecture

```text
                   Product engineering inputs
      graph / event stream / test evidence / spectra / node states
                              |
                  Experiment specification (V3)
                              |
   +----------+----------+----------+----------+----------+----------+
   | Quantum  | Neuro    | Bayesian | Photonic | Cellular | Reversible| Reservoir
   | QAOA     | LIF      | Beta     | MZI mesh | 1D/2D CA | gate net  | ESN
   +----------+----------+----------+----------+----------+----------+
                              |
               JSON result + algorithm metadata + seed
                              |
              Classical baseline / review / decision
                              |
              Per-use-case Docker image + logged testcase
```

V2 keeps V1's integration model: no web service, database, cloud dependency or hardware driver. Each engine is a small pure-Python module with explicit inputs and JSON-serializable outputs. The CLI is the integration surface, and Docker provides isolated per-use-case execution. A multi-engine orchestration harness is deferred to V3.

## Constraints

- Quantum statevector dimension is `2**n`; V1 limits n to 10 and p=1 QAOA with a deterministic grid.
- LIF uses a single scalar neuron and simple current input; it is not an SNN training framework.
- Bayesian tail probability uses midpoint numerical integration; it is decision support, not certification.
- Photonic MZI phases are searched by deterministic coordinate descent on a synthetic phase-encoded dataset; energy numbers are heuristic photon counts, not device measurements.
- Cellular automata use binary grids with wrap or zero boundaries; consensus results depend on seed, noise and topology.
- Reversible circuits retain garbage bits; logical reversibility does not make a physical implementation lossless.
- ESN reservoir weights are fixed and seeded; only the ridge readout is trained. Spectral radius is estimated by power iteration.
- Synthetic examples are not validated production datasets. No cross-engine advantage claims are made.
