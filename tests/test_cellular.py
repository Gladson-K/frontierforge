import unittest

from frontierforge.cellular import ca1d_step, ca2d_step, load_consensus


class CellularTest(unittest.TestCase):
    def test_rule_90_is_xor_of_neighbours(self):
        self.assertEqual(ca1d_step([0, 0, 1, 0, 0], 90, 'wrap'), [0, 1, 0, 1, 0])
        self.assertEqual(ca1d_step([0, 0, 1, 0, 0], 90, 'zero'), [0, 1, 0, 1, 0])

    def test_life_blinker_has_period_two(self):
        grid = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
        ]
        after_one = ca2d_step(grid, 'life', 'zero')
        after_two = ca2d_step(after_one, 'life', 'zero')
        self.assertNotEqual(after_one, grid)
        self.assertEqual(after_two, grid)

    def test_majority_consensus_improves_agreement(self):
        result = load_consensus(size=12, steps=30, noise=0.15, seed=11)
        self.assertGreaterEqual(result['final_agreement'], result['initial_agreement'])
        self.assertTrue(result['local_majority_correct'])
        self.assertLessEqual(result['final_agreement'], 1.0)
        self.assertGreaterEqual(result['centralized_global_mean_threshold_agreement'], 0.0)

    def test_invalid_rules_raise(self):
        with self.assertRaises(ValueError):
            ca1d_step([0, 1], 256)
        with self.assertRaises(ValueError):
            ca2d_step([[0, 1], [1, 0]], 'unknown')
        with self.assertRaises(ValueError):
            load_consensus(size=1)


if __name__ == '__main__':
    unittest.main()
