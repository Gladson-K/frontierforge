# FrontierForge V2 test results

- Generated (UTC): `2026-11-24T16:10:36+00:00`
- Python: `3.12.3`
- Branch: `dev/v2`
- Commit: `9bd9bd1`
- Commands passed: `21/21`
- Testcase lines captured: `60`
- Docker pipelines included: `True`

Every command below is recorded even when it fails; full combined stdout/stderr is preserved in the log blocks. A green status here is local verification evidence, not a product safety or legal claim.

## Summary

| # | Kind | Command | Exit | Seconds | Testcases | Status |
| --- | --- | --- | ---: | ---: | ---: | --- |
| 1 | local | `.venv/bin/python -m unittest discover -s tests -v` | 0 | 1.191 | 20 | PASS |
| 2 | local | `.venv/bin/python -m unittest discover -s tests -p test_engines.py -v` | 0 | 0.316 | 4 | PASS |
| 3 | local | `.venv/bin/python -m unittest discover -s tests -p test_photonic.py -v` | 0 | 0.323 | 4 | PASS |
| 4 | local | `.venv/bin/python -m unittest discover -s tests -p test_cellular.py -v` | 0 | 0.229 | 4 | PASS |
| 5 | local | `.venv/bin/python -m unittest discover -s tests -p test_reversible.py -v` | 0 | 0.313 | 4 | PASS |
| 6 | local | `.venv/bin/python -m unittest discover -s tests -p test_reservoir.py -v` | 0 | 0.416 | 4 | PASS |
| 7 | cli | `.venv/bin/python -m frontierforge.cli quantum-demo` | 0 | 0.376 | 0 | PASS |
| 8 | cli | `.venv/bin/python -m frontierforge.cli neuro-demo` | 0 | 1.281 | 0 | PASS |
| 9 | cli | `.venv/bin/python -m frontierforge.cli risk` | 0 | 1.098 | 0 | PASS |
| 10 | cli | `.venv/bin/python -m frontierforge.cli photonic-demo` | 0 | 1.248 | 0 | PASS |
| 11 | cli | `.venv/bin/python -m frontierforge.cli ca-demo` | 0 | 1.012 | 0 | PASS |
| 12 | cli | `.venv/bin/python -m frontierforge.cli reversible-demo` | 0 | 0.711 | 0 | PASS |
| 13 | cli | `.venv/bin/python -m frontierforge.cli reservoir-demo` | 0 | 0.845 | 0 | PASS |
| 14 | docker | `docker build -f docker/Dockerfile.quantum -t frontierforge:quantum . && docker run --rm frontierforge:quantum` | 0 | 6.252 | 0 | PASS |
| 15 | docker | `docker build -f docker/Dockerfile.neuro -t frontierforge:neuro . && docker run --rm frontierforge:neuro` | 0 | 5.972 | 0 | PASS |
| 16 | docker | `docker build -f docker/Dockerfile.bayes -t frontierforge:bayes . && docker run --rm frontierforge:bayes` | 0 | 5.204 | 0 | PASS |
| 17 | docker | `docker build -f docker/Dockerfile.photonic -t frontierforge:photonic . && docker run --rm frontierforge:photonic` | 0 | 4.146 | 0 | PASS |
| 18 | docker | `docker build -f docker/Dockerfile.cellular -t frontierforge:cellular . && docker run --rm frontierforge:cellular` | 0 | 4.594 | 0 | PASS |
| 19 | docker | `docker build -f docker/Dockerfile.reversible -t frontierforge:reversible . && docker run --rm frontierforge:reversible` | 0 | 7.9 | 0 | PASS |
| 20 | docker | `docker build -f docker/Dockerfile.reservoir -t frontierforge:reservoir . && docker run --rm frontierforge:reservoir` | 0 | 4.942 | 0 | PASS |
| 21 | docker | `docker build -f docker/Dockerfile.tests -t frontierforge:tests . && docker run --rm frontierforge:tests` | 0 | 13.394 | 20 | PASS |

## 1. local — .venv/bin/python -m unittest discover -s tests -v

- Exit code: `0`
- Duration: `1.191s`

### Testcase results

| Test | Module | Result |
| --- | --- | --- |
| `test_invalid_rules_raise` | `test_cellular.CellularTest.test_invalid_rules_raise` | `ok` |
| `test_life_blinker_has_period_two` | `test_cellular.CellularTest.test_life_blinker_has_period_two` | `ok` |
| `test_majority_consensus_improves_agreement` | `test_cellular.CellularTest.test_majority_consensus_improves_agreement` | `ok` |
| `test_rule_90_is_xor_of_neighbours` | `test_cellular.CellularTest.test_rule_90_is_xor_of_neighbours` | `ok` |
| `test_bayes` | `test_engines.EnginesTest.test_bayes` | `ok` |
| `test_burst` | `test_engines.EnginesTest.test_burst` | `ok` |
| `test_lif` | `test_engines.EnginesTest.test_lif` | `ok` |
| `test_quantum` | `test_engines.EnginesTest.test_quantum` | `ok` |
| `test_coherent_classifier_beats_intensity_baseline` | `test_photonic.PhotonicTest.test_coherent_classifier_beats_intensity_baseline` | `ok` |
| `test_mesh_layout_and_size` | `test_photonic.PhotonicTest.test_mesh_layout_and_size` | `ok` |
| `test_mesh_matches_dense_matmul` | `test_photonic.PhotonicTest.test_mesh_matches_dense_matmul` | `ok` |
| `test_mzi_is_unitary` | `test_photonic.PhotonicTest.test_mzi_is_unitary` | `ok` |
| `test_cholesky_solves_spd_system` | `test_reservoir.ReservoirTest.test_cholesky_solves_spd_system` | `ok` |
| `test_esn_beats_persistence_baseline` | `test_reservoir.ReservoirTest.test_esn_beats_persistence_baseline` | `ok` |
| `test_reservoir_states_are_deterministic_and_bounded` | `test_reservoir.ReservoirTest.test_reservoir_states_are_deterministic_and_bounded` | `ok` |
| `test_ridge_fit_is_deterministic` | `test_reservoir.ReservoirTest.test_ridge_fit_is_deterministic` | `ok` |
| `test_circuit_is_reversible` | `test_reversible.ReversibleTest.test_circuit_is_reversible` | `ok` |
| `test_full_adder_truth_table` | `test_reversible.ReversibleTest.test_full_adder_truth_table` | `ok` |
| `test_gate_counts_depth_and_validation` | `test_reversible.ReversibleTest.test_gate_counts_depth_and_validation` | `ok` |
| `test_landauer_bound_is_positive_but_lower_bound_only` | `test_reversible.ReversibleTest.test_landauer_bound_is_positive_but_lower_bound_only` | `ok` |

### Full log

````text
test_invalid_rules_raise (test_cellular.CellularTest.test_invalid_rules_raise) ... ok
test_life_blinker_has_period_two (test_cellular.CellularTest.test_life_blinker_has_period_two) ... ok
test_majority_consensus_improves_agreement (test_cellular.CellularTest.test_majority_consensus_improves_agreement) ... ok
test_rule_90_is_xor_of_neighbours (test_cellular.CellularTest.test_rule_90_is_xor_of_neighbours) ... ok
test_bayes (test_engines.EnginesTest.test_bayes) ... ok
test_burst (test_engines.EnginesTest.test_burst) ... ok
test_lif (test_engines.EnginesTest.test_lif) ... ok
test_quantum (test_engines.EnginesTest.test_quantum) ... ok
test_coherent_classifier_beats_intensity_baseline (test_photonic.PhotonicTest.test_coherent_classifier_beats_intensity_baseline) ... ok
test_mesh_layout_and_size (test_photonic.PhotonicTest.test_mesh_layout_and_size) ... ok
test_mesh_matches_dense_matmul (test_photonic.PhotonicTest.test_mesh_matches_dense_matmul) ... ok
test_mzi_is_unitary (test_photonic.PhotonicTest.test_mzi_is_unitary) ... ok
test_cholesky_solves_spd_system (test_reservoir.ReservoirTest.test_cholesky_solves_spd_system) ... ok
test_esn_beats_persistence_baseline (test_reservoir.ReservoirTest.test_esn_beats_persistence_baseline) ... ok
test_reservoir_states_are_deterministic_and_bounded (test_reservoir.ReservoirTest.test_reservoir_states_are_deterministic_and_bounded) ... ok
test_ridge_fit_is_deterministic (test_reservoir.ReservoirTest.test_ridge_fit_is_deterministic) ... ok
test_circuit_is_reversible (test_reversible.ReversibleTest.test_circuit_is_reversible) ... ok
test_full_adder_truth_table (test_reversible.ReversibleTest.test_full_adder_truth_table) ... ok
test_gate_counts_depth_and_validation (test_reversible.ReversibleTest.test_gate_counts_depth_and_validation) ... ok
test_landauer_bound_is_positive_but_lower_bound_only (test_reversible.ReversibleTest.test_landauer_bound_is_positive_but_lower_bound_only) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.327s

OK
````

## 2. local — .venv/bin/python -m unittest discover -s tests -p test_engines.py -v

- Exit code: `0`
- Duration: `0.316s`

### Testcase results

| Test | Module | Result |
| --- | --- | --- |
| `test_bayes` | `test_engines.EnginesTest.test_bayes` | `ok` |
| `test_burst` | `test_engines.EnginesTest.test_burst` | `ok` |
| `test_lif` | `test_engines.EnginesTest.test_lif` | `ok` |
| `test_quantum` | `test_engines.EnginesTest.test_quantum` | `ok` |

### Full log

````text
test_bayes (test_engines.EnginesTest.test_bayes) ... ok
test_burst (test_engines.EnginesTest.test_burst) ... ok
test_lif (test_engines.EnginesTest.test_lif) ... ok
test_quantum (test_engines.EnginesTest.test_quantum) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.007s

OK
````

## 3. local — .venv/bin/python -m unittest discover -s tests -p test_photonic.py -v

- Exit code: `0`
- Duration: `0.323s`

### Testcase results

| Test | Module | Result |
| --- | --- | --- |
| `test_coherent_classifier_beats_intensity_baseline` | `test_photonic.PhotonicTest.test_coherent_classifier_beats_intensity_baseline` | `ok` |
| `test_mesh_layout_and_size` | `test_photonic.PhotonicTest.test_mesh_layout_and_size` | `ok` |
| `test_mesh_matches_dense_matmul` | `test_photonic.PhotonicTest.test_mesh_matches_dense_matmul` | `ok` |
| `test_mzi_is_unitary` | `test_photonic.PhotonicTest.test_mzi_is_unitary` | `ok` |

### Full log

````text
test_coherent_classifier_beats_intensity_baseline (test_photonic.PhotonicTest.test_coherent_classifier_beats_intensity_baseline) ... ok
test_mesh_layout_and_size (test_photonic.PhotonicTest.test_mesh_layout_and_size) ... ok
test_mesh_matches_dense_matmul (test_photonic.PhotonicTest.test_mesh_matches_dense_matmul) ... ok
test_mzi_is_unitary (test_photonic.PhotonicTest.test_mzi_is_unitary) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.094s

OK
````

## 4. local — .venv/bin/python -m unittest discover -s tests -p test_cellular.py -v

- Exit code: `0`
- Duration: `0.229s`

### Testcase results

| Test | Module | Result |
| --- | --- | --- |
| `test_invalid_rules_raise` | `test_cellular.CellularTest.test_invalid_rules_raise` | `ok` |
| `test_life_blinker_has_period_two` | `test_cellular.CellularTest.test_life_blinker_has_period_two` | `ok` |
| `test_majority_consensus_improves_agreement` | `test_cellular.CellularTest.test_majority_consensus_improves_agreement` | `ok` |
| `test_rule_90_is_xor_of_neighbours` | `test_cellular.CellularTest.test_rule_90_is_xor_of_neighbours` | `ok` |

### Full log

````text
test_invalid_rules_raise (test_cellular.CellularTest.test_invalid_rules_raise) ... ok
test_life_blinker_has_period_two (test_cellular.CellularTest.test_life_blinker_has_period_two) ... ok
test_majority_consensus_improves_agreement (test_cellular.CellularTest.test_majority_consensus_improves_agreement) ... ok
test_rule_90_is_xor_of_neighbours (test_cellular.CellularTest.test_rule_90_is_xor_of_neighbours) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.005s

OK
````

## 5. local — .venv/bin/python -m unittest discover -s tests -p test_reversible.py -v

- Exit code: `0`
- Duration: `0.313s`

### Testcase results

| Test | Module | Result |
| --- | --- | --- |
| `test_circuit_is_reversible` | `test_reversible.ReversibleTest.test_circuit_is_reversible` | `ok` |
| `test_full_adder_truth_table` | `test_reversible.ReversibleTest.test_full_adder_truth_table` | `ok` |
| `test_gate_counts_depth_and_validation` | `test_reversible.ReversibleTest.test_gate_counts_depth_and_validation` | `ok` |
| `test_landauer_bound_is_positive_but_lower_bound_only` | `test_reversible.ReversibleTest.test_landauer_bound_is_positive_but_lower_bound_only` | `ok` |

### Full log

````text
test_circuit_is_reversible (test_reversible.ReversibleTest.test_circuit_is_reversible) ... ok
test_full_adder_truth_table (test_reversible.ReversibleTest.test_full_adder_truth_table) ... ok
test_gate_counts_depth_and_validation (test_reversible.ReversibleTest.test_gate_counts_depth_and_validation) ... ok
test_landauer_bound_is_positive_but_lower_bound_only (test_reversible.ReversibleTest.test_landauer_bound_is_positive_but_lower_bound_only) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.003s

OK
````

## 6. local — .venv/bin/python -m unittest discover -s tests -p test_reservoir.py -v

- Exit code: `0`
- Duration: `0.416s`

### Testcase results

| Test | Module | Result |
| --- | --- | --- |
| `test_cholesky_solves_spd_system` | `test_reservoir.ReservoirTest.test_cholesky_solves_spd_system` | `ok` |
| `test_esn_beats_persistence_baseline` | `test_reservoir.ReservoirTest.test_esn_beats_persistence_baseline` | `ok` |
| `test_reservoir_states_are_deterministic_and_bounded` | `test_reservoir.ReservoirTest.test_reservoir_states_are_deterministic_and_bounded` | `ok` |
| `test_ridge_fit_is_deterministic` | `test_reservoir.ReservoirTest.test_ridge_fit_is_deterministic` | `ok` |

### Full log

````text
test_cholesky_solves_spd_system (test_reservoir.ReservoirTest.test_cholesky_solves_spd_system) ... ok
test_esn_beats_persistence_baseline (test_reservoir.ReservoirTest.test_esn_beats_persistence_baseline) ... ok
test_reservoir_states_are_deterministic_and_bounded (test_reservoir.ReservoirTest.test_reservoir_states_are_deterministic_and_bounded) ... ok
test_ridge_fit_is_deterministic (test_reservoir.ReservoirTest.test_ridge_fit_is_deterministic) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.135s

OK
````

## 7. cli — .venv/bin/python -m frontierforge.cli quantum-demo

- Exit code: `0`
- Duration: `0.376s`

### Full log

````text
{
  "engine": "qaoa_statevector_cpu",
  "qubits": 4,
  "edges": [
    [
      0,
      1
    ],
    [
      1,
      2
    ],
    [
      2,
      3
    ],
    [
      3,
      0
    ],
    [
      0,
      2
    ]
  ],
  "p": 1,
  "gamma": 0.5235987755982988,
  "beta": 1.9198621771937623,
  "expected_cut": 3.224007726050861,
  "most_likely_bitstring_q0_first": "1010",
  "sampled_bitstring_cut": 4,
  "statevector_dimension": 16,
  "note": "Exact statevector simulation, not execution on quantum hardware."
}
````

## 8. cli — .venv/bin/python -m frontierforge.cli neuro-demo

- Exit code: `0`
- Duration: `1.281s`

### Full log

````text
{
  "lif": {
    "engine": "lif_event_simulator_cpu",
    "steps": 17,
    "spike_times": [
      4,
      7,
      11,
      16
    ],
    "spike_count": 4,
    "membrane_trace": [
      0.0,
      0.0,
      0.2,
      0.47,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.1,
      0.885,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    "note": "Software simulation of a simple spiking neuron; no neuromorphic chip required."
  },
  "burst_analysis": {
    "engine": "event_burst_detector_cpu",
    "windows": 6,
    "bursts": [
      {
        "start": 1,
        "end": 4,
        "events": 3
      },
      {
        "start": 2,
        "end": 5,
        "events": 3
      },
      {
        "start": 7,
        "end": 10,
        "events": 3
      },
      {
        "start": 8,
        "end": 11,
        "events": 3
      },
      {
        "start": 9,
        "end": 12,
        "events": 4
      },
      {
        "start": 10,
        "end": 13,
        "events": 3
      }
    ],
    "note": "Illustrative event-based detector; tune thresholds on representative product data."
  }
}
````

## 9. cli — .venv/bin/python -m frontierforge.cli risk

- Exit code: `0`
- Duration: `1.098s`

### Full log

````text
{
  "engine": "beta_binomial_risk_cpu",
  "observed_failures": 3,
  "trials": 40,
  "posterior_alpha": 4.0,
  "posterior_beta": 46.0,
  "posterior_mean_failure_rate": 0.08,
  "posterior_stddev": 0.037988646394705367,
  "risk_threshold": 0.1,
  "probability_true_failure_rate_exceeds_threshold": 0.2647659539626636,
  "decision": "within_threshold",
  "note": "Bayesian estimate from test evidence; not a guarantee of future field reliability."
}
````

## 10. cli — .venv/bin/python -m frontierforge.cli photonic-demo

- Exit code: `0`
- Duration: `1.248s`

### Full log

````text
{
  "engine": "photonic_mzi_mesh_cpu",
  "ports": 4,
  "classes": 2,
  "mesh_layers": 4,
  "mzis": 6,
  "phase_parameters": 12,
  "train_samples": 60,
  "test_samples": 60,
  "train_accuracy": 1.0,
  "test_accuracy": 1.0,
  "baseline_intensity_nearest_centroid_accuracy": 0.45,
  "coherent_mesh_beats_intensity_baseline": true,
  "mesh_unitarity_error": 0.0,
  "mesh_vs_dense_matmul_max_deviation": 0.0,
  "wavelength_nm": 1550.0,
  "photon_energy_joules": 1.2815779723541474e-19,
  "estimated_complex_ops_per_inference": 12,
  "energy_per_inference_1_photon_per_op_joules": 1.5378935668249768e-18,
  "note": "Coherent-interference simulation; the synthetic classes differ only in optical phase. Energy figures are single-photon heuristics, not measured hardware power."
}
````

## 11. cli — .venv/bin/python -m frontierforge.cli ca-demo

- Exit code: `0`
- Duration: `1.012s`

### Full log

````text
{
  "engine": "cellular_automata_cpu",
  "grid_size": 12,
  "steps": 30,
  "noise_probability": 0.15,
  "noise_flips": 17,
  "underlying_truth": 1,
  "initial_agreement": 0.5833333333333334,
  "initial_disagreement": 0.41666666666666663,
  "final_value": 1,
  "final_agreement": 0.7916666666666666,
  "consensus_reached": false,
  "consensus_step": null,
  "local_majority_correct": true,
  "centralized_global_mean_threshold_value": 1,
  "centralized_global_mean_threshold_agreement": 0.5833333333333334,
  "note": "Local majority CA reaches agreement using only neighbourhood reads; the baseline needs all readings for a global mean. Illustrative only."
}
````

## 12. cli — .venv/bin/python -m frontierforge.cli reversible-demo

- Exit code: `0`
- Duration: `0.711s`

### Full log

````text
{
  "engine": "reversible_logic_cpu",
  "wires": 4,
  "gate_counts": {
    "TOFFOLI": 2,
    "CNOT": 2
  },
  "gate_count": 4,
  "circuit_depth": 4,
  "ancilla_bits": 1,
  "garbage_bits": 2,
  "truth_table": [
    {
      "a": 0,
      "b": 0,
      "cin": 0,
      "sum": 0,
      "carry": 0,
      "expected_sum": 0,
      "expected_carry": 0,
      "pass": true
    },
    {
      "a": 0,
      "b": 0,
      "cin": 1,
      "sum": 1,
      "carry": 0,
      "expected_sum": 1,
      "expected_carry": 0,
      "pass": true
    },
    {
      "a": 0,
      "b": 1,
      "cin": 0,
      "sum": 1,
      "carry": 0,
      "expected_sum": 1,
      "expected_carry": 0,
      "pass": true
    },
    {
      "a": 0,
      "b": 1,
      "cin": 1,
      "sum": 0,
      "carry": 1,
      "expected_sum": 0,
      "expected_carry": 1,
      "pass": true
    },
    {
      "a": 1,
      "b": 0,
      "cin": 0,
      "sum": 1,
      "carry": 0,
      "expected_sum": 1,
      "expected_carry": 0,
      "pass": true
    },
    {
      "a": 1,
      "b": 0,
      "cin": 1,
      "sum": 0,
      "carry": 1,
      "expected_sum": 0,
      "expected_carry": 1,
      "pass": true
    },
    {
      "a": 1,
      "b": 1,
      "cin": 0,
      "sum": 0,
      "carry": 1,
      "expected_sum": 0,
      "expected_carry": 1,
      "pass": true
    },
    {
      "a": 1,
      "b": 1,
      "cin": 1,
      "sum": 1,
      "carry": 1,
      "expected_sum": 1,
      "expected_carry": 1,
      "pass": true
    }
  ],
  "truth_table_pass": true,
  "bijective": true,
  "inverse_roundtrip_pass": true,
  "landauer": {
    "temperature_kelvin": 300.15,
    "energy_per_erased_bit_joules": 2.8724143745212633e-21,
    "irreversible_adder_min_bits_erased": 1,
    "irreversible_adder_min_energy_joules": 2.8724143745212633e-21,
    "reversible_adder_min_energy_joules": 0.0
  },
  "note": "Logical reversibility is exact here; Landauer values are theoretical lower bounds for bit erasure, not measured device energy."
}
````

## 13. cli — .venv/bin/python -m frontierforge.cli reservoir-demo

- Exit code: `0`
- Duration: `0.845s`

### Full log

````text
{
  "engine": "reservoir_computing_cpu",
  "units": 40,
  "connectivity": 0.15,
  "spectral_radius_target": 0.9,
  "spectral_radius_estimate": 0.9799420350461011,
  "leak": 0.3,
  "washout": 50,
  "series_length": 300,
  "train_fraction": 0.6,
  "test_points": 100,
  "esn_nmse": 0.05493122603484217,
  "ar_order": 5,
  "ar_nmse": 0.0028452301163674676,
  "persistence_nmse": 3.133119614835914,
  "esn_beats_persistence": true,
  "esn_beats_ar": false,
  "note": "Only the linear readout is trained; reservoir weights are fixed and seeded. Comparison is on one synthetic series, not a field dataset."
}
````

## 14. docker — docker build -f docker/Dockerfile.quantum -t frontierforge:quantum . && docker run --rm frontierforge:quantum

- Exit code: `0`
- Duration: `6.252s`

### Full log

````text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon    194kB

Step 1/6 : FROM python:3.12-slim
 ---> 191083cdf6c7
Step 2/6 : ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 ---> Using cache
 ---> 0a7d2771a244
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> d4bdf794cdcd
Step 4/6 : COPY pyproject.toml ./
 ---> Using cache
 ---> 840b054cc809
Step 5/6 : COPY frontierforge ./frontierforge
 ---> Using cache
 ---> f2690322a8f1
Step 6/6 : CMD ["python", "-m", "frontierforge.cli", "quantum-demo"]
 ---> Using cache
 ---> 99099066e2ce
Successfully built 99099066e2ce
Successfully tagged frontierforge:quantum
{
  "engine": "qaoa_statevector_cpu",
  "qubits": 4,
  "edges": [
    [
      0,
      1
    ],
    [
      1,
      2
    ],
    [
      2,
      3
    ],
    [
      3,
      0
    ],
    [
      0,
      2
    ]
  ],
  "p": 1,
  "gamma": 0.5235987755982988,
  "beta": 1.9198621771937623,
  "expected_cut": 3.224007726050861,
  "most_likely_bitstring_q0_first": "1010",
  "sampled_bitstring_cut": 4,
  "statevector_dimension": 16,
  "note": "Exact statevector simulation, not execution on quantum hardware."
}
````

## 15. docker — docker build -f docker/Dockerfile.neuro -t frontierforge:neuro . && docker run --rm frontierforge:neuro

- Exit code: `0`
- Duration: `5.972s`

### Full log

````text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon    194kB

Step 1/6 : FROM python:3.12-slim
 ---> 191083cdf6c7
Step 2/6 : ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 ---> Using cache
 ---> 0a7d2771a244
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> d4bdf794cdcd
Step 4/6 : COPY pyproject.toml ./
 ---> Using cache
 ---> 840b054cc809
Step 5/6 : COPY frontierforge ./frontierforge
 ---> Using cache
 ---> f2690322a8f1
Step 6/6 : CMD ["python", "-m", "frontierforge.cli", "neuro-demo"]
 ---> Using cache
 ---> b69f07d83a36
Successfully built b69f07d83a36
Successfully tagged frontierforge:neuro
{
  "lif": {
    "engine": "lif_event_simulator_cpu",
    "steps": 17,
    "spike_times": [
      4,
      7,
      11,
      16
    ],
    "spike_count": 4,
    "membrane_trace": [
      0.0,
      0.0,
      0.2,
      0.47,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.1,
      0.885,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0,
      0.0
    ],
    "note": "Software simulation of a simple spiking neuron; no neuromorphic chip required."
  },
  "burst_analysis": {
    "engine": "event_burst_detector_cpu",
    "windows": 6,
    "bursts": [
      {
        "start": 1,
        "end": 4,
        "events": 3
      },
      {
        "start": 2,
        "end": 5,
        "events": 3
      },
      {
        "start": 7,
        "end": 10,
        "events": 3
      },
      {
        "start": 8,
        "end": 11,
        "events": 3
      },
      {
        "start": 9,
        "end": 12,
        "events": 4
      },
      {
        "start": 10,
        "end": 13,
        "events": 3
      }
    ],
    "note": "Illustrative event-based detector; tune thresholds on representative product data."
  }
}
````

## 16. docker — docker build -f docker/Dockerfile.bayes -t frontierforge:bayes . && docker run --rm frontierforge:bayes

- Exit code: `0`
- Duration: `5.204s`

### Full log

````text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon    194kB

Step 1/6 : FROM python:3.12-slim
 ---> 191083cdf6c7
Step 2/6 : ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 ---> Using cache
 ---> 0a7d2771a244
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> d4bdf794cdcd
Step 4/6 : COPY pyproject.toml ./
 ---> Using cache
 ---> 840b054cc809
Step 5/6 : COPY frontierforge ./frontierforge
 ---> Using cache
 ---> f2690322a8f1
Step 6/6 : CMD ["python", "-m", "frontierforge.cli", "risk", "--failures", "3", "--trials", "40"]
 ---> Using cache
 ---> df36de7e9839
Successfully built df36de7e9839
Successfully tagged frontierforge:bayes
{
  "engine": "beta_binomial_risk_cpu",
  "observed_failures": 3,
  "trials": 40,
  "posterior_alpha": 4.0,
  "posterior_beta": 46.0,
  "posterior_mean_failure_rate": 0.08,
  "posterior_stddev": 0.037988646394705367,
  "risk_threshold": 0.1,
  "probability_true_failure_rate_exceeds_threshold": 0.2647659539626636,
  "decision": "within_threshold",
  "note": "Bayesian estimate from test evidence; not a guarantee of future field reliability."
}
````

## 17. docker — docker build -f docker/Dockerfile.photonic -t frontierforge:photonic . && docker run --rm frontierforge:photonic

- Exit code: `0`
- Duration: `4.146s`

### Full log

````text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon    194kB

Step 1/6 : FROM python:3.12-slim
 ---> 191083cdf6c7
Step 2/6 : ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 ---> Using cache
 ---> 0a7d2771a244
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> d4bdf794cdcd
Step 4/6 : COPY pyproject.toml ./
 ---> Using cache
 ---> 840b054cc809
Step 5/6 : COPY frontierforge ./frontierforge
 ---> Using cache
 ---> f2690322a8f1
Step 6/6 : CMD ["python", "-m", "frontierforge.cli", "photonic-demo"]
 ---> Using cache
 ---> 459bf805c72f
Successfully built 459bf805c72f
Successfully tagged frontierforge:photonic
{
  "engine": "photonic_mzi_mesh_cpu",
  "ports": 4,
  "classes": 2,
  "mesh_layers": 4,
  "mzis": 6,
  "phase_parameters": 12,
  "train_samples": 60,
  "test_samples": 60,
  "train_accuracy": 1.0,
  "test_accuracy": 1.0,
  "baseline_intensity_nearest_centroid_accuracy": 0.45,
  "coherent_mesh_beats_intensity_baseline": true,
  "mesh_unitarity_error": 0.0,
  "mesh_vs_dense_matmul_max_deviation": 0.0,
  "wavelength_nm": 1550.0,
  "photon_energy_joules": 1.2815779723541474e-19,
  "estimated_complex_ops_per_inference": 12,
  "energy_per_inference_1_photon_per_op_joules": 1.5378935668249768e-18,
  "note": "Coherent-interference simulation; the synthetic classes differ only in optical phase. Energy figures are single-photon heuristics, not measured hardware power."
}
````

## 18. docker — docker build -f docker/Dockerfile.cellular -t frontierforge:cellular . && docker run --rm frontierforge:cellular

- Exit code: `0`
- Duration: `4.594s`

### Full log

````text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon    194kB

Step 1/6 : FROM python:3.12-slim
 ---> 191083cdf6c7
Step 2/6 : ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 ---> Using cache
 ---> 0a7d2771a244
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> d4bdf794cdcd
Step 4/6 : COPY pyproject.toml ./
 ---> Using cache
 ---> 840b054cc809
Step 5/6 : COPY frontierforge ./frontierforge
 ---> Using cache
 ---> f2690322a8f1
Step 6/6 : CMD ["python", "-m", "frontierforge.cli", "ca-demo"]
 ---> Using cache
 ---> e0ab1024d175
Successfully built e0ab1024d175
Successfully tagged frontierforge:cellular
{
  "engine": "cellular_automata_cpu",
  "grid_size": 12,
  "steps": 30,
  "noise_probability": 0.15,
  "noise_flips": 17,
  "underlying_truth": 1,
  "initial_agreement": 0.5833333333333334,
  "initial_disagreement": 0.41666666666666663,
  "final_value": 1,
  "final_agreement": 0.7916666666666666,
  "consensus_reached": false,
  "consensus_step": null,
  "local_majority_correct": true,
  "centralized_global_mean_threshold_value": 1,
  "centralized_global_mean_threshold_agreement": 0.5833333333333334,
  "note": "Local majority CA reaches agreement using only neighbourhood reads; the baseline needs all readings for a global mean. Illustrative only."
}
````

## 19. docker — docker build -f docker/Dockerfile.reversible -t frontierforge:reversible . && docker run --rm frontierforge:reversible

- Exit code: `0`
- Duration: `7.9s`

### Full log

````text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon    194kB

Step 1/6 : FROM python:3.12-slim
 ---> 191083cdf6c7
Step 2/6 : ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 ---> Using cache
 ---> 0a7d2771a244
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> d4bdf794cdcd
Step 4/6 : COPY pyproject.toml ./
 ---> Using cache
 ---> 840b054cc809
Step 5/6 : COPY frontierforge ./frontierforge
 ---> Using cache
 ---> f2690322a8f1
Step 6/6 : CMD ["python", "-m", "frontierforge.cli", "reversible-demo"]
 ---> Using cache
 ---> 3c2814856cec
Successfully built 3c2814856cec
Successfully tagged frontierforge:reversible
{
  "engine": "reversible_logic_cpu",
  "wires": 4,
  "gate_counts": {
    "TOFFOLI": 2,
    "CNOT": 2
  },
  "gate_count": 4,
  "circuit_depth": 4,
  "ancilla_bits": 1,
  "garbage_bits": 2,
  "truth_table": [
    {
      "a": 0,
      "b": 0,
      "cin": 0,
      "sum": 0,
      "carry": 0,
      "expected_sum": 0,
      "expected_carry": 0,
      "pass": true
    },
    {
      "a": 0,
      "b": 0,
      "cin": 1,
      "sum": 1,
      "carry": 0,
      "expected_sum": 1,
      "expected_carry": 0,
      "pass": true
    },
    {
      "a": 0,
      "b": 1,
      "cin": 0,
      "sum": 1,
      "carry": 0,
      "expected_sum": 1,
      "expected_carry": 0,
      "pass": true
    },
    {
      "a": 0,
      "b": 1,
      "cin": 1,
      "sum": 0,
      "carry": 1,
      "expected_sum": 0,
      "expected_carry": 1,
      "pass": true
    },
    {
      "a": 1,
      "b": 0,
      "cin": 0,
      "sum": 1,
      "carry": 0,
      "expected_sum": 1,
      "expected_carry": 0,
      "pass": true
    },
    {
      "a": 1,
      "b": 0,
      "cin": 1,
      "sum": 0,
      "carry": 1,
      "expected_sum": 0,
      "expected_carry": 1,
      "pass": true
    },
    {
      "a": 1,
      "b": 1,
      "cin": 0,
      "sum": 0,
      "carry": 1,
      "expected_sum": 0,
      "expected_carry": 1,
      "pass": true
    },
    {
      "a": 1,
      "b": 1,
      "cin": 1,
      "sum": 1,
      "carry": 1,
      "expected_sum": 1,
      "expected_carry": 1,
      "pass": true
    }
  ],
  "truth_table_pass": true,
  "bijective": true,
  "inverse_roundtrip_pass": true,
  "landauer": {
    "temperature_kelvin": 300.15,
    "energy_per_erased_bit_joules": 2.8724143745212633e-21,
    "irreversible_adder_min_bits_erased": 1,
    "irreversible_adder_min_energy_joules": 2.8724143745212633e-21,
    "reversible_adder_min_energy_joules": 0.0
  },
  "note": "Logical reversibility is exact here; Landauer values are theoretical lower bounds for bit erasure, not measured device energy."
}
````

## 20. docker — docker build -f docker/Dockerfile.reservoir -t frontierforge:reservoir . && docker run --rm frontierforge:reservoir

- Exit code: `0`
- Duration: `4.942s`

### Full log

````text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon    194kB

Step 1/6 : FROM python:3.12-slim
 ---> 191083cdf6c7
Step 2/6 : ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 ---> Using cache
 ---> 0a7d2771a244
Step 3/6 : WORKDIR /app
 ---> Using cache
 ---> d4bdf794cdcd
Step 4/6 : COPY pyproject.toml ./
 ---> Using cache
 ---> 840b054cc809
Step 5/6 : COPY frontierforge ./frontierforge
 ---> Using cache
 ---> f2690322a8f1
Step 6/6 : CMD ["python", "-m", "frontierforge.cli", "reservoir-demo"]
 ---> Using cache
 ---> 30037c0356f0
Successfully built 30037c0356f0
Successfully tagged frontierforge:reservoir
{
  "engine": "reservoir_computing_cpu",
  "units": 40,
  "connectivity": 0.15,
  "spectral_radius_target": 0.9,
  "spectral_radius_estimate": 0.9799420350461011,
  "leak": 0.3,
  "washout": 50,
  "series_length": 300,
  "train_fraction": 0.6,
  "test_points": 100,
  "esn_nmse": 0.05493122603484217,
  "ar_order": 5,
  "ar_nmse": 0.0028452301163674676,
  "persistence_nmse": 3.133119614835914,
  "esn_beats_persistence": true,
  "esn_beats_ar": false,
  "note": "Only the linear readout is trained; reservoir weights are fixed and seeded. Comparison is on one synthetic series, not a field dataset."
}
````

## 21. docker — docker build -f docker/Dockerfile.tests -t frontierforge:tests . && docker run --rm frontierforge:tests

- Exit code: `0`
- Duration: `13.394s`

### Testcase results

| Test | Module | Result |
| --- | --- | --- |
| `test_invalid_rules_raise` | `test_cellular.CellularTest.test_invalid_rules_raise` | `ok` |
| `test_life_blinker_has_period_two` | `test_cellular.CellularTest.test_life_blinker_has_period_two` | `ok` |
| `test_majority_consensus_improves_agreement` | `test_cellular.CellularTest.test_majority_consensus_improves_agreement` | `ok` |
| `test_rule_90_is_xor_of_neighbours` | `test_cellular.CellularTest.test_rule_90_is_xor_of_neighbours` | `ok` |
| `test_bayes` | `test_engines.EnginesTest.test_bayes` | `ok` |
| `test_burst` | `test_engines.EnginesTest.test_burst` | `ok` |
| `test_lif` | `test_engines.EnginesTest.test_lif` | `ok` |
| `test_quantum` | `test_engines.EnginesTest.test_quantum` | `ok` |
| `test_coherent_classifier_beats_intensity_baseline` | `test_photonic.PhotonicTest.test_coherent_classifier_beats_intensity_baseline` | `ok` |
| `test_mesh_layout_and_size` | `test_photonic.PhotonicTest.test_mesh_layout_and_size` | `ok` |
| `test_mesh_matches_dense_matmul` | `test_photonic.PhotonicTest.test_mesh_matches_dense_matmul` | `ok` |
| `test_mzi_is_unitary` | `test_photonic.PhotonicTest.test_mzi_is_unitary` | `ok` |
| `test_cholesky_solves_spd_system` | `test_reservoir.ReservoirTest.test_cholesky_solves_spd_system` | `ok` |
| `test_esn_beats_persistence_baseline` | `test_reservoir.ReservoirTest.test_esn_beats_persistence_baseline` | `ok` |
| `test_reservoir_states_are_deterministic_and_bounded` | `test_reservoir.ReservoirTest.test_reservoir_states_are_deterministic_and_bounded` | `ok` |
| `test_ridge_fit_is_deterministic` | `test_reservoir.ReservoirTest.test_ridge_fit_is_deterministic` | `ok` |
| `test_circuit_is_reversible` | `test_reversible.ReversibleTest.test_circuit_is_reversible` | `ok` |
| `test_full_adder_truth_table` | `test_reversible.ReversibleTest.test_full_adder_truth_table` | `ok` |
| `test_gate_counts_depth_and_validation` | `test_reversible.ReversibleTest.test_gate_counts_depth_and_validation` | `ok` |
| `test_landauer_bound_is_positive_but_lower_bound_only` | `test_reversible.ReversibleTest.test_landauer_bound_is_positive_but_lower_bound_only` | `ok` |

### Full log

````text
DEPRECATED: The legacy builder is deprecated and will be removed in a future release.
            Install the buildx component to build images with BuildKit:
            https://docs.docker.com/go/buildx/

Sending build context to Docker daemon    194kB

Step 1/7 : FROM python:3.12-slim
 ---> 191083cdf6c7
Step 2/7 : ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
 ---> Using cache
 ---> 0a7d2771a244
Step 3/7 : WORKDIR /app
 ---> Using cache
 ---> d4bdf794cdcd
Step 4/7 : COPY pyproject.toml ./
 ---> Using cache
 ---> 840b054cc809
Step 5/7 : COPY frontierforge ./frontierforge
 ---> Using cache
 ---> f2690322a8f1
Step 6/7 : COPY tests ./tests
 ---> 84c5b779fbe5
Step 7/7 : CMD ["python", "-m", "unittest", "discover", "-s", "tests", "-v"]
 ---> Running in d917e0fcbdf1
 ---> Removed intermediate container d917e0fcbdf1
 ---> 54fd6962c2a5
Successfully built 54fd6962c2a5
Successfully tagged frontierforge:tests
test_invalid_rules_raise (test_cellular.CellularTest.test_invalid_rules_raise) ... ok
test_life_blinker_has_period_two (test_cellular.CellularTest.test_life_blinker_has_period_two) ... ok
test_majority_consensus_improves_agreement (test_cellular.CellularTest.test_majority_consensus_improves_agreement) ... ok
test_rule_90_is_xor_of_neighbours (test_cellular.CellularTest.test_rule_90_is_xor_of_neighbours) ... ok
test_bayes (test_engines.EnginesTest.test_bayes) ... ok
test_burst (test_engines.EnginesTest.test_burst) ... ok
test_lif (test_engines.EnginesTest.test_lif) ... ok
test_quantum (test_engines.EnginesTest.test_quantum) ... ok
test_coherent_classifier_beats_intensity_baseline (test_photonic.PhotonicTest.test_coherent_classifier_beats_intensity_baseline) ... ok
test_mesh_layout_and_size (test_photonic.PhotonicTest.test_mesh_layout_and_size) ... ok
test_mesh_matches_dense_matmul (test_photonic.PhotonicTest.test_mesh_matches_dense_matmul) ... ok
test_mzi_is_unitary (test_photonic.PhotonicTest.test_mzi_is_unitary) ... ok
test_cholesky_solves_spd_system (test_reservoir.ReservoirTest.test_cholesky_solves_spd_system) ... ok
test_esn_beats_persistence_baseline (test_reservoir.ReservoirTest.test_esn_beats_persistence_baseline) ... ok
test_reservoir_states_are_deterministic_and_bounded (test_reservoir.ReservoirTest.test_reservoir_states_are_deterministic_and_bounded) ... ok
test_ridge_fit_is_deterministic (test_reservoir.ReservoirTest.test_ridge_fit_is_deterministic) ... ok
test_circuit_is_reversible (test_reversible.ReversibleTest.test_circuit_is_reversible) ... ok
test_full_adder_truth_table (test_reversible.ReversibleTest.test_full_adder_truth_table) ... ok
test_gate_counts_depth_and_validation (test_reversible.ReversibleTest.test_gate_counts_depth_and_validation) ... ok
test_landauer_bound_is_positive_but_lower_bound_only (test_reversible.ReversibleTest.test_landauer_bound_is_positive_but_lower_bound_only) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.303s

OK
````
