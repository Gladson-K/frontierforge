import unittest

from frontierforge.reservoir import (
    cholesky_solve,
    make_reservoir,
    ridge_fit,
    reservoir_forecast,
    reservoir_states,
    synthetic_maintenance_series,
)


class ReservoirTest(unittest.TestCase):
    def test_cholesky_solves_spd_system(self):
        matrix = [[4.0, 1.0], [1.0, 3.0]]
        rhs = [1.0, 2.0]
        solution = cholesky_solve(matrix, rhs)
        residual = max(abs(sum(matrix[i][j] * solution[j] for j in range(2)) - rhs[i])
                       for i in range(2))
        self.assertLess(residual, 1e-12)
        with self.assertRaises(ValueError):
            cholesky_solve([[1.0, 2.0], [2.0, 1.0]], [1.0, 1.0])

    def test_ridge_fit_is_deterministic(self):
        features = [[1.0, 0.5], [0.5, 1.0], [0.2, 0.9]]
        targets = [1.0, 1.4, 1.2]
        first = ridge_fit(features, targets)
        second = ridge_fit(features, targets)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 2)

    def test_reservoir_states_are_deterministic_and_bounded(self):
        weights, input_weights = make_reservoir(12, connectivity=0.3, seed=5)
        again, again_inputs = make_reservoir(12, connectivity=0.3, seed=5)
        self.assertEqual(weights, again)
        self.assertEqual(input_weights, again_inputs)
        series = synthetic_maintenance_series(40, seed=3)
        first = reservoir_states(series, weights, input_weights)
        second = reservoir_states(series, weights, input_weights)
        self.assertEqual(first, second)
        self.assertTrue(all(abs(value) <= 1.0 for row in first for value in row))

    def test_esn_beats_persistence_baseline(self):
        result = reservoir_forecast(length=300, units=40, seed=3)
        self.assertTrue(result['esn_beats_persistence'])
        self.assertGreater(result['test_points'], 0)
        self.assertGreaterEqual(result['esn_nmse'], 0.0)
        self.assertGreater(result['persistence_nmse'], result['esn_nmse'])


if __name__ == '__main__':
    unittest.main()
