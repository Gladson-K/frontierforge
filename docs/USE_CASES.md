# Three differentiated use cases

## A. Quantum-assisted architecture and resource planning
**Product scenario:** choose a compatible set of compute modules, services or build tasks under cost, capacity and dependency constraints. Represent binary choices as a graph/QUBO/Ising objective, use a QAOA-style circuit to explore candidate solutions, and compare against exact or heuristic classical baselines.

**V1 slice:** small MaxCut instance with statevector QAOA p=1. It demonstrates circuit-based optimization and exposes the probability distribution/expected objective. It does not solve arbitrary QUBO constraints yet.

**Potential product value:** early exploration of hard combinatorial choices such as test scheduling, placement, resource allocation and feature selection. Quantum advantage is not assumed; the platform must report classical baseline quality and runtime.

## B. Neuromorphic event-native product intelligence
**Product scenario:** a low-power product (industrial sensor, battery system, wearable, robotics platform) emits sparse events. A conventional pipeline may repeatedly process dense samples even when little changes. An event-driven network integrates signals over time and emits spikes only when accumulated evidence crosses a threshold.

**V1 slice:** LIF neuron simulation and sliding-window burst detector using synthetic event streams.

**Potential product value:** event-triggered anomaly detection, wake-word-like temporal patterns, predictive maintenance and low-power control. Validate against conventional thresholding/ML on the same dataset before claiming energy or accuracy benefits.

## C. Bayesian uncertainty-aware release engineering
**Product scenario:** a product team has limited test evidence. A binary pass/fail rate is uncertain, especially early in development. Bayesian updating combines prior assumptions with observed test outcomes and estimates the probability that the underlying failure rate exceeds a release threshold.

**V1 slice:** Beta-Binomial posterior mean, standard deviation and posterior tail probability.

**Potential product value:** risk-aware test prioritization, staged rollout decisions, reliability estimation and explicit uncertainty reporting. Prior selection must be visible and sensitivity-tested; this is decision support, not certification.

## Why these are distinct
They exercise three different computational models: complex-amplitude state evolution, asynchronous event/spike dynamics, and probabilistic inference over uncertain parameters. They are not simply three industry verticals wrapped around the same CRUD application.
