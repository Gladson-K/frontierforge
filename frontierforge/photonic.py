"""Photonic Mach-Zehnder interferometer (MZI) mesh demonstrator.

Simulates a small Clements-style mesh of tunable 2x2 beamsplitters acting on
complex optical amplitudes.  Used as an illustrative coherent linear classifier:
a phase-encoded synthetic spectrum that is invisible to intensity-only sensors
becomes separable after coherent interference.  Pure CPU float/complex maths.

This is a numerical model, not a claim about photonic hardware performance.
"""
from __future__ import annotations
import cmath, math, random

PLANCK_J_S = 6.62607015e-34
LIGHT_SPEED_M_S = 299792458.0
DEFAULT_WAVELENGTH_M = 1.55e-6
PHOTON_ENERGY_J = PLANCK_J_S * LIGHT_SPEED_M_S / DEFAULT_WAVELENGTH_M


def mzi_matrix(theta, phi):
    """2x2 tunable MZI transfer matrix; unitary for all real theta, phi."""
    c, s = math.cos(theta), math.sin(theta)
    e = cmath.exp(1j * phi)
    return ((e * c, -e * s), (s, c))


def mesh_layout(ports):
    """Alternating even/odd layers of adjacent MZI pairs (Clements-style)."""
    if ports < 2:
        raise ValueError('mesh requires at least 2 ports')
    layout = []
    for layer in range(ports):
        start = layer % 2
        pairs = [(i, i + 1) for i in range(start, ports - 1, 2)]
        if pairs:
            layout.append(pairs)
    return layout


def num_mzis(ports):
    return sum(len(layer) for layer in mesh_layout(ports))


def mesh_apply(phases, amplitudes):
    """Propagate complex amplitudes through the mesh.

    ``phases`` is a flat list of ``(theta, phi)`` tuples in mesh order.
    Returns a new list of output complex amplitudes.
    """
    layout = mesh_layout(len(amplitudes))
    if len(phases) != sum(len(layer) for layer in layout):
        raise ValueError('phase count does not match mesh size')
    v = list(amplitudes)
    k = 0
    for layer in layout:
        for i, j in layer:
            m = mzi_matrix(*phases[k])
            k += 1
            a, b = v[i], v[j]
            v[i] = m[0][0] * a + m[0][1] * b
            v[j] = m[1][0] * a + m[1][1] * b
    return v


def mesh_matrix(phases, ports):
    """Full ``ports x ports`` unitary built column by column from basis inputs."""
    if len(phases) != num_mzis(ports):
        raise ValueError('phase count does not match mesh size')
    cols = []
    for j in range(ports):
        basis = [0j] * ports
        basis[j] = 1 + 0j
        cols.append(mesh_apply(phases, basis))
    return [[cols[j][i] for j in range(ports)] for i in range(ports)]


def dense_matvec(matrix, vector):
    """Plain complex matrix-vector multiply (classical float baseline)."""
    n = len(matrix)
    return [sum(matrix[i][j] * vector[j] for j in range(n)) for i in range(n)]


def mesh_unitarity_error(phases, ports):
    """Max deviation of U^dagger U from the identity."""
    u = mesh_matrix(phases, ports)
    err = 0.0
    for a in range(ports):
        for b in range(ports):
            dot = sum(u[k][a].conjugate() * u[k][b] for k in range(ports))
            err = max(err, abs(dot - (1.0 if a == b else 0.0)))
    return err


def mesh_vs_matmul_deviation(phases, amplitudes):
    """Max deviation between mesh propagation and a dense matmul baseline."""
    u = mesh_matrix(phases, len(amplitudes))
    dense = dense_matvec(u, amplitudes)
    mesh = mesh_apply(phases, amplitudes)
    return max(abs(x - y) for x, y in zip(dense, mesh))


def spectral_phase_dataset(ports, per_class, seed, noise=0.04):
    """Synthetic 2-class spectra with identical band intensity, opposite phase.

    Classes share |amplitude| per band, so intensity-only measurements cannot
    separate them; coherent mixing can.
    """
    if ports < 2:
        raise ValueError('need at least 2 ports')
    rng = random.Random(seed)
    mag = 1.0 / math.sqrt(2.0)
    samples, labels = [], []
    for label in (0, 1):
        rel_phase = 0.0 if label == 0 else math.pi
        for _ in range(per_class):
            ideal = [0j] * ports
            ideal[0] = mag
            ideal[1] = mag * cmath.exp(1j * rel_phase)
            for p in range(2, ports):
                ideal[p] = complex(rng.uniform(-0.08, 0.08), rng.uniform(-0.08, 0.08))
            v = [x + complex(rng.uniform(-noise, noise), rng.uniform(-noise, noise))
                 for x in ideal]
            norm = math.sqrt(sum(abs(x) ** 2 for x in v))
            samples.append([x / norm for x in v])
            labels.append(label)
    return samples, labels


def _intensity_features(vector):
    return [abs(x) ** 2 for x in vector]


def intensity_nearest_centroid_accuracy(train, train_labels, test, test_labels, classes=2):
    """Classical baseline: nearest class centroid in intensity-only feature space."""
    centroids = [[0.0] * len(train[0]) for _ in range(classes)]
    counts = [0] * classes
    for vec, label in zip(train, train_labels):
        feats = _intensity_features(vec)
        for p, f in enumerate(feats):
            centroids[label][p] += f
        counts[label] += 1
    for c in range(classes):
        if counts[c]:
            centroids[c] = [x / counts[c] for x in centroids[c]]
    correct = 0
    for vec, label in zip(test, test_labels):
        feats = _intensity_features(vec)
        dists = [sum((feats[p] - centroids[c][p]) ** 2 for p in range(len(feats)))
                 for c in range(classes)]
        if dists.index(min(dists)) == label:
            correct += 1
    return correct / len(test)


def _accuracy_and_margin(phases, samples, labels, classes):
    correct, margin = 0, 0.0
    for vec, label in zip(samples, labels):
        out = mesh_apply(phases, vec)
        inten = [abs(out[c]) ** 2 for c in range(classes)]
        pred = inten.index(max(inten))
        correct += pred == label
        other = max(inten[c] for c in range(classes) if c != label)
        margin += inten[label] - other
    return correct, margin


def train_mesh_classifier(samples, labels, classes=2, sweeps=6):
    """Deterministic coordinate search over MZI phases.

    Starts from the identity mesh and greedily accepts phase offsets that
    improve (correct count, then summed label margin).  No stochastic search.
    """
    ports = len(samples[0])
    total = num_mzis(ports)
    phases = [(0.0, 0.0)] * total
    offsets = (math.pi / 4, -math.pi / 4, math.pi / 8, -math.pi / 8,
               math.pi / 16, -math.pi / 16, math.pi / 2, -math.pi / 2)
    best = _accuracy_and_margin(phases, samples, labels, classes)
    for _ in range(sweeps):
        improved = False
        for idx in range(total):
            for which in (0, 1):
                for delta in offsets:
                    trial = list(phases)
                    theta, phi = trial[idx]
                    if which == 0:
                        theta += delta
                    else:
                        phi += delta
                    trial[idx] = (theta, phi)
                    score = _accuracy_and_margin(trial, samples, labels, classes)
                    if score > best:
                        phases, best = trial, score
                        improved = True
        if not improved:
            break
    return phases


def photonic_classifier(ports=4, per_class=30, seed=7, sweeps=6, noise=0.04):
    """Train/evaluate the coherent mesh classifier and report diagnostics."""
    if ports < 3:
        raise ValueError('demo needs at least 3 ports (2 classes + slack)')
    if per_class < 2:
        raise ValueError('per_class must be >= 2')
    train_x, train_y = spectral_phase_dataset(ports, per_class, seed, noise)
    test_x, test_y = spectral_phase_dataset(ports, per_class, seed + 1000, noise)
    phases = train_mesh_classifier(train_x, train_y, classes=2, sweeps=sweeps)

    train_correct, _ = _accuracy_and_margin(phases, train_x, train_y, 2)
    test_correct, _ = _accuracy_and_margin(phases, test_x, test_y, 2)
    baseline = intensity_nearest_centroid_accuracy(train_x, train_y, test_x, test_y)

    layout = mesh_layout(ports)
    mzi_count = num_mzis(ports)
    ops_per_inference = 2 * mzi_count
    return {
        'engine': 'photonic_mzi_mesh_cpu',
        'ports': ports,
        'classes': 2,
        'mesh_layers': len(layout),
        'mzis': mzi_count,
        'phase_parameters': 2 * mzi_count,
        'train_samples': len(train_x),
        'test_samples': len(test_x),
        'train_accuracy': train_correct / len(train_x),
        'test_accuracy': test_correct / len(test_x),
        'baseline_intensity_nearest_centroid_accuracy': baseline,
        'coherent_mesh_beats_intensity_baseline': (test_correct / len(test_x)) > baseline,
        'mesh_unitarity_error': mesh_unitarity_error(phases, ports),
        'mesh_vs_dense_matmul_max_deviation': mesh_vs_matmul_deviation(phases, train_x[0]),
        'wavelength_nm': DEFAULT_WAVELENGTH_M * 1e9,
        'photon_energy_joules': PHOTON_ENERGY_J,
        'estimated_complex_ops_per_inference': ops_per_inference,
        'energy_per_inference_1_photon_per_op_joules': ops_per_inference * PHOTON_ENERGY_J,
        'note': ('Coherent-interference simulation; the synthetic classes differ only '
                 'in optical phase. Energy figures are single-photon heuristics, not '
                 'measured hardware power.'),
    }
