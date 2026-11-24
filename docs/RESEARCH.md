# Research notes and technology landscape

Research snapshot prepared 5 November 2026, extended for V2 on 24 November 2026. “Emerging” does not mean unused: these fields have active research communities, but remain less routine in everyday application delivery than CPU/GPU software stacks.

## Quantum and hybrid quantum-classical computing
- Qiskit provides an open-source quantum software stack for algorithms, transpilation and heterogeneous execution. https://www.ibm.com/quantum/qiskit
- NVIDIA CUDA-Q provides a hybrid programming model spanning CPUs, GPUs, QPUs and simulators. https://nvidia.github.io/cuda-quantum/
- PennyLane provides differentiable quantum programming and simulator backends. https://pennylane.ai/
- Product implication: build against a simulator first, retain a classical baseline, and treat QPU execution as an optional adapter. Statevector simulation is exponential and does not imply quantum speedup.

## Neuromorphic and event-based computing
- Intel describes neuromorphic research and the Lava software framework for neuro-inspired applications. https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html
- Lava is intended to prototype neuro-inspired applications on conventional processors and map them to supported heterogeneous targets. https://lava-nc.org/
- Product implication: event-native representations can help sensors and temporal signals, but accuracy, latency and energy must be measured against a fair baseline.

## Photonic computing
- Reck et al. described experimental realisation of arbitrary unitary transformations using beam splitters and phase shifters, the basis of programmable interferometer meshes.
- Clements et al. described an efficient rectangular decomposition for universal linear optics, motivating the layered MZI layout used here.
- Product implication: coherent interference can implement linear layers optically, but loss, phase stability, detection and conversion costs must be measured. This repository simulates complex amplitudes on a CPU only.

## Cellular automata and self-organisation
- Wolfram's elementary cellular automata provide a compact model of local rules producing global patterns; rule 90 is equivalent to XOR of neighbour states.
- Conway's Game of Life and majority-rule automata illustrate emergent behaviour from local updates.
- Product implication: local-only coordination is attractive for constrained edge networks, but convergence depends on topology and initial conditions. Report the actual consensus outcome.

## Reversible logic and Landauer's principle
- Landauer argued that logically irreversible bit erasure has a minimum energy cost of `k_B T ln 2` per erased bit.
- Fredkin, Toffoli and CNOT gates allow boolean functions to be embedded in reversible circuits when garbage bits are retained.
- Product implication: logical reversibility is exact in the simulator; physical energy benefit requires hardware evidence and accounting for garbage disposal.

## Reservoir computing
- Jaeger's echo state networks and Maass et al.'s liquid state machines fixed a random recurrent reservoir and trained only a linear readout.
- Ridge regression with seeded fixed weights gives a small reproducible forecasting baseline.
- Product implication: useful as an auditable temporal baseline, not a claim of accuracy advantage over tuned AR, Kalman or learned models.

## Digital twins and co-simulation (adjacent extension)
- OpenModelica and the Functional Mock-up Interface ecosystem support equation-based modelling and co-simulation. https://modelica.org/tools/ and https://fmi-standard.org/tools/
- A later V3/V4 orchestration layer could couple these models with engines; it is not part of the V2 kernels.

## V2 scope choice
The implementation uses no third-party runtime dependencies, runs on CPU, and records seeds and diagnostics. Optional adapters or hardware backends should remain separate so the reference results stay reproducible.
