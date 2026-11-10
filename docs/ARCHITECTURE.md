# Architecture

```text
                  Product engineering inputs
        graph / event stream / test evidence + assumptions
                             |
                 Experiment specification (future)
                             |
        +--------------------+--------------------+
        |                    |                    |
  Quantum engine       Neuromorphic engine    Bayesian engine
  statevector/QAOA     LIF/event windows      Beta posterior
        |                    |                    |
        +--------------------+--------------------+
                             |
              JSON result + algorithm metadata
                             |
             Classical baseline / review / decision
```

V1 intentionally has no web service, database, cloud dependency or hardware driver. Each engine is a small pure-Python module with explicit inputs and JSON-serializable outputs. The CLI is the integration surface. This keeps the computational core reproducible and makes future adapters optional.

## Constraints
- Quantum statevector dimension is `2**n`; V1 limits n to 10.
- QAOA implements p=1 and a deterministic coarse grid, not a general-purpose optimizer.
- LIF uses a single scalar neuron and simple current input; it is not a full SNN training framework.
- Bayesian tail probability uses midpoint numerical integration; it is a compact teaching/decision-support implementation.
- Synthetic examples are not validated production datasets.
