"""Echo-state-network (reservoir computing) demonstrator.

A seeded sparse random recurrent reservoir drives a leaky tanh state, and only
a ridge-regression readout is trained.  Includes a pure-Python Cholesky solver,
plus AR(p) and persistence baselines on a synthetic predictive-maintenance
signal.  CPU-only, no third-party dependencies.
"""
from __future__ import annotations
import math, random


def cholesky_solve(matrix, rhs):
    """Solve A x = b for symmetric positive-definite A via Cholesky."""
    n = len(matrix)
    if n == 0 or len(rhs) != n or any(len(row) != n for row in matrix):
        raise ValueError('matrix must be square and match rhs length')
    lower = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            acc = sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                pivot = matrix[i][i] - acc
                if pivot <= 0:
                    raise ValueError('matrix is not positive-definite')
                lower[i][j] = math.sqrt(pivot)
            else:
                lower[i][j] = (matrix[i][j] - acc) / lower[j][j]
    y = [0.0] * n
    for i in range(n):
        y[i] = (rhs[i] - sum(lower[i][k] * y[k] for k in range(i))) / lower[i][i]
    x = [0.0] * n
    for i in reversed(range(n)):
        x[i] = (y[i] - sum(lower[k][i] * x[k] for k in range(i + 1, n))) / lower[i][i]
    return x


def ridge_fit(features, targets, ridge=1e-6):
    """Closed-form ridge regression using the Cholesky solver."""
    if not features or len(features) != len(targets):
        raise ValueError('features and targets must be non-empty and aligned')
    rows, cols = len(features), len(features[0])
    gram = [[0.0] * cols for _ in range(cols)]
    moment = [0.0] * cols
    for row, target in zip(features, targets):
        for i in range(cols):
            moment[i] += row[i] * target
            for j in range(cols):
                gram[i][j] += row[i] * row[j]
    for i in range(cols):
        gram[i][i] += ridge
    return cholesky_solve(gram, moment)


def make_reservoir(units, connectivity=0.15, spectral_radius=0.9, seed=0):
    """Seeded sparse random reservoir scaled to a target spectral radius."""
    if units < 2:
        raise ValueError('units must be >= 2')
    if not 0.0 < connectivity <= 1.0:
        raise ValueError('connectivity must be in (0, 1]')
    if spectral_radius <= 0:
        raise ValueError('spectral_radius must be positive')
    rng = random.Random(seed)
    weights = [[0.0] * units for _ in range(units)]
    for i in range(units):
        for j in range(units):
            if rng.random() < connectivity:
                weights[i][j] = rng.uniform(-0.5, 0.5)
    radius = _spectral_radius_estimate(weights, rng)
    if radius == 0:
        raise ValueError('reservoir collapsed to all zeros; increase connectivity')
    scale = spectral_radius / radius
    weights = [[value * scale for value in row] for row in weights]
    input_weights = [rng.uniform(-0.5, 0.5) for _ in range(units)]
    return weights, input_weights


def _spectral_radius_estimate(weights, rng, iterations=60):
    n = len(weights)
    vector = [rng.uniform(-1.0, 1.0) for _ in range(n)]
    norm = math.sqrt(sum(v * v for v in vector))
    vector = [v / norm for v in vector]
    estimate = 0.0
    for _ in range(iterations):
        applied = [sum(weights[i][j] * vector[j] for j in range(n)) for i in range(n)]
        estimate = math.sqrt(sum(v * v for v in applied))
        if estimate == 0:
            return 0.0
        vector = [v / estimate for v in applied]
    return estimate


def reservoir_states(series, weights, input_weights, leak=0.3):
    if not 0.0 < leak <= 1.0:
        raise ValueError('leak must be in (0, 1]')
    units = len(weights)
    state = [0.0] * units
    states = []
    for value in series:
        pre = [input_weights[i] * value
               + sum(weights[i][j] * state[j] for j in range(units))
               for i in range(units)]
        state = [(1.0 - leak) * state[i] + leak * math.tanh(pre[i]) for i in range(units)]
        states.append(state[:])
    return states


def synthetic_maintenance_series(length, seed=3):
    """Load signal with drift, seasonality, degradation ramp and noise."""
    if length < 10:
        raise ValueError('length must be >= 10')
    rng = random.Random(seed)
    series = []
    ramp_start = int(length * 0.6)
    for t in range(length):
        drift = 0.02 * t
        seasonal = 2.0 * math.sin(2.0 * math.pi * t / 48.0)
        degradation = 0.0
        if t >= ramp_start:
            degradation = 0.8 * math.exp((t - ramp_start) / 35.0) - 0.8
        noise = rng.uniform(-0.3, 0.3)
        series.append(50.0 + drift + seasonal + degradation + noise)
    return series


def _nmse(actual, predicted):
    mean = sum(actual) / len(actual)
    denominator = sum((value - mean) ** 2 for value in actual)
    numerator = sum((a - p) ** 2 for a, p in zip(actual, predicted))
    return numerator / denominator if denominator else 0.0


def _one_step_esn(series, weights, input_weights, leak, washout, train_fraction, ridge):
    states = reservoir_states(series, weights, input_weights, leak)
    features = states[washout:-1]
    targets = series[washout + 1:]
    split = int(len(features) * train_fraction)
    if split < 2:
        raise ValueError('series too short for the requested split')
    readout = ridge_fit(features[:split], targets[:split], ridge)
    predictions = [sum(w * f for w, f in zip(readout, row)) for row in features[split:]]
    return targets[split:], predictions


def _one_step_ar(series, order, washout, train_fraction, ridge):
    features = [[series[t - k] for k in range(1, order + 1)] for t in range(washout, len(series) - 1)]
    targets = series[washout + 1:]
    split = int(len(features) * train_fraction)
    readout = ridge_fit(features[:split], targets[:split], ridge)
    predictions = [sum(w * f for w, f in zip(readout, row)) for row in features[split:]]
    return targets[split:], predictions


def reservoir_forecast(length=300, units=40, seed=3, connectivity=0.15,
                       spectral_radius=0.9, leak=0.3, washout=50,
                       train_fraction=0.6, ridge=1e-6, ar_order=5):
    """One-step-ahead forecast comparison: ESN vs AR(5) vs persistence."""
    if train_fraction <= 0 or train_fraction >= 1:
        raise ValueError('train_fraction must be in (0, 1)')
    series = synthetic_maintenance_series(length, seed)
    weights, input_weights = make_reservoir(units, connectivity, spectral_radius, seed)
    radius_estimate = _spectral_radius_estimate(weights, random.Random(seed))

    esn_targets, esn_predictions = _one_step_esn(
        series, weights, input_weights, leak, washout, train_fraction, ridge)
    ar_targets, ar_predictions = _one_step_ar(
        series, ar_order, washout, train_fraction, ridge)
    persistence_predictions = [series[t - 1] for t in range(washout + 1, len(series))]

    esn_nmse = _nmse(esn_targets, esn_predictions)
    ar_nmse = _nmse(ar_targets, ar_predictions)
    persistence_nmse = _nmse(esn_targets, persistence_predictions)
    return {
        'engine': 'reservoir_computing_cpu',
        'units': units,
        'connectivity': connectivity,
        'spectral_radius_target': spectral_radius,
        'spectral_radius_estimate': radius_estimate,
        'leak': leak,
        'washout': washout,
        'series_length': length,
        'train_fraction': train_fraction,
        'test_points': len(esn_targets),
        'esn_nmse': esn_nmse,
        'ar_order': ar_order,
        'ar_nmse': ar_nmse,
        'persistence_nmse': persistence_nmse,
        'esn_beats_persistence': esn_nmse < persistence_nmse,
        'esn_beats_ar': esn_nmse < ar_nmse,
        'note': ('Only the linear readout is trained; reservoir weights are fixed and '
                 'seeded. Comparison is on one synthetic series, not a field dataset.'),
    }
