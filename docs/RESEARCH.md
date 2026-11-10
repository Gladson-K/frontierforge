# Research notes and technology landscape

Research snapshot prepared 5 November 2026. “Emerging” does not mean unused: these fields have active research communities and mature-enough open tools, but remain less routine in everyday application delivery than CPU/GPU software stacks.

## Quantum and hybrid quantum-classical computing
- Qiskit provides an open-source quantum software stack for algorithms, transpilation and heterogeneous execution. Official overview: https://www.ibm.com/quantum/qiskit
- NVIDIA CUDA-Q provides a hybrid programming model spanning CPUs, GPUs, QPUs and simulators, with Python and C++ interfaces. Documentation: https://nvidia.github.io/cuda-quantum/
- PennyLane provides differentiable quantum programming and simulator backends. https://pennylane.ai/
- Product implication: build against a simulator first, retain a classical baseline, and treat QPU execution as an optional adapter. Small statevector simulation is exponential and does not imply quantum speedup.

## Neuromorphic and event-based computing
- Intel describes neuromorphic research and the Lava software framework for neuro-inspired applications and Loihi hardware. https://www.intel.com/content/www/us/en/research/neuromorphic-computing.html
- Lava is an open-source framework intended to prototype neuro-inspired applications on conventional processors and map them to supported heterogeneous/neuromorphic targets. https://lava-nc.org/
- Product implication: event-native representations and sparse computation can be useful for sensors and temporal signals, but accuracy, latency and energy must be measured against a fair conventional baseline.

## Digital twins and co-simulation (adjacent extension)
- The Modelica tools ecosystem includes OpenModelica for equation-based modeling and simulation. https://modelica.org/tools/
- FMI defines model exchange and co-simulation interfaces; its tools directory lists open simulation and digital-twin projects. https://fmi-standard.org/tools/
- Product implication: a later fourth engine could couple software, physical-process and controller models before hardware exists. This is a valuable extension but is not one of the three V1 computational kernels.

## V1 scope choice
The implementation uses no third-party runtime dependencies and is CPU-only. The three selected kernels are small enough to inspect, test and run on a developer laptop. Integrations with Qiskit, CUDA-Q, PennyLane or Lava should be optional backends, not hard dependencies.
