# Seven differentiated use cases

## V1 use cases

### A. Quantum-assisted architecture and resource planning
**Product scenario:** choose compatible compute modules, services or build tasks under cost, capacity and dependency constraints. Represent binary choices as a graph/QUBO/Ising objective, use a QAOA-style circuit to explore candidates, and compare with classical baselines.

**V1 slice:** small MaxCut instance with statevector QAOA p=1, reporting the expected objective and probability distribution. Quantum advantage is not assumed.

### B. Neuromorphic event-native product intelligence
**Product scenario:** a low-power product emits sparse events; an event-driven network integrates signals and emits spikes only when accumulated evidence crosses a threshold.

**V1 slice:** LIF neuron simulation and sliding-window burst detector on a synthetic event stream. Accuracy, latency and energy must be measured against a fair conventional baseline before any benefit claim.

### C. Bayesian uncertainty-aware release engineering
**Product scenario:** early test evidence leaves the true pass/fail rate uncertain. Beta-Binomial updating estimates the probability that the failure rate exceeds a release threshold.

**V1 slice:** posterior mean, standard deviation and tail probability. Prior choice must be visible and sensitivity-tested; this is decision support, not certification.

## V2 use cases

### D. Photonic coherent spectral classification
**Product scenario:** edge sensors produce weak spectral patterns whose phases carry information that intensity-only readout discards. A programmable optical linear layer could perform classification before digitisation.

**V2 slice:** a Clements-style MZI mesh is trained by deterministic coordinate descent on complex amplitudes. Synthetic classes share per-band intensity and differ mainly in phase, so an intensity nearest-centroid baseline performs near chance while the coherent mesh separates them.

**Potential value:** exploratory edge-sensor preprocessing. Photon-energy figures are theoretical one-photon-per-operation heuristics, not measured hardware power.

### E. Cellular-automata load consensus
**Product scenario:** many edge nodes hold noisy local binary readings and must agree on a load state without a central collector.

**V2 slice:** von Neumann majority automata use only neighbour states; results are compared with a global-mean threshold baseline that requires every reading. The demo reports agreement improvement, final value, whether full consensus occurred, and the step count.

**Potential value:** local-first coordination studies. The baseline has more information, so comparisons describe information locality, not speed superiority.

### F. Reversible embedded controller logic
**Product scenario:** an embedded controller performs arithmetic whose logical irreversibility would erase bits and dissipate at least the Landauer bound per erased bit.

**V2 slice:** a reversible full adder uses two Toffoli and two CNOT gates with one clean ancilla. Truth table, bijectivity, inverse round trip and gate depth are checked; the irreversible minimum is compared with the theoretical reversible minimum of zero.

**Potential value:** understanding when retaining garbage bits avoids logical erasure. Physical devices still dissipate energy, and uncomputing garbage is not free.

### G. Reservoir computing for predictive maintenance
**Product scenario:** sensor trajectories need short-horizon forecasting without training a large recurrent model.

**V2 slice:** a seeded echo-state network with a pure-Python ridge readout is compared with AR(5) and persistence on a synthetic degradation trace using one-step-ahead held-out NMSE.

**Potential value:** a small auditable baseline for temporal forecasting. Results are from one synthetic series and are not field validation.

## Why these are distinct
They exercise different computational models: complex-amplitude state evolution, asynchronous event/spike dynamics, probabilistic inference, coherent interferometric linear algebra, local discrete dynamics, reversible boolean permutations and fixed-random recurrent dynamics. They are computational experiments, not variations of the same CRUD application.
