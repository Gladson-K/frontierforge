import unittest
import math

from frontierforge.photonic import (
    mzi_matrix,
    mesh_layout,
    num_mzis,
    mesh_apply,
    mesh_matrix,
    dense_matvec,
    mesh_unitarity_error,
    photonic_classifier,
)


class PhotonicTest(unittest.TestCase):
    def test_mzi_is_unitary(self):
        m = mzi_matrix(0.37, 1.21)
        for i in (0, 1):
            for j in (0, 1):
                dot = sum(m[k][i].conjugate() * m[k][j] for k in (0, 1))
                self.assertAlmostEqual(dot, 1.0 if i == j else 0.0, places=12)

    def test_mesh_layout_and_size(self):
        layout = mesh_layout(4)
        self.assertEqual(len(layout), 4)
        self.assertEqual(num_mzis(4), 6)
        self.assertEqual(layout[0], [(0, 1), (2, 3)])
        self.assertEqual(layout[1], [(1, 2)])

    def test_mesh_matches_dense_matmul(self):
        phases = [(0.2 * i, 0.3 * i) for i in range(num_mzis(4))]
        amplitudes = [complex(0.5, 0.1), 0.7, complex(-0.2, 0.3), 0.4]
        deviation = max(abs(a - b) for a, b in zip(
            mesh_apply(phases, amplitudes), dense_matvec(mesh_matrix(phases, 4), amplitudes)))
        self.assertLess(deviation, 1e-12)
        self.assertLess(mesh_unitarity_error(phases, 4), 1e-12)

    def test_coherent_classifier_beats_intensity_baseline(self):
        result = photonic_classifier(ports=4, per_class=24, seed=7, sweeps=4)
        self.assertGreaterEqual(result['test_accuracy'], 0.9)
        self.assertGreater(result['test_accuracy'],
                           result['baseline_intensity_nearest_centroid_accuracy'])
        self.assertTrue(result['coherent_mesh_beats_intensity_baseline'])
        self.assertLess(result['mesh_unitarity_error'], 1e-12)
        self.assertTrue(math.isfinite(result['photon_energy_joules']))


if __name__ == '__main__':
    unittest.main()
