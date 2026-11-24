import unittest

from frontierforge.reversible import (
    analyze_full_adder,
    circuit_depth,
    full_adder_circuit,
    gate_counts,
    inverse_circuit,
    is_bijective,
    landauer_bound,
    run_reversible,
)


class ReversibleTest(unittest.TestCase):
    def test_full_adder_truth_table(self):
        result = analyze_full_adder()
        self.assertTrue(result['truth_table_pass'])
        self.assertEqual(len(result['truth_table']), 8)
        for row in result['truth_table']:
            self.assertEqual(row['sum'], row['expected_sum'])
            self.assertEqual(row['carry'], row['expected_carry'])

    def test_circuit_is_reversible(self):
        circuit = full_adder_circuit()
        self.assertTrue(is_bijective(circuit, 4))
        inverted = inverse_circuit(circuit)
        for value in range(16):
            bits = [(value >> q) & 1 for q in range(4)]
            self.assertEqual(run_reversible(run_reversible(bits, circuit), inverted), bits)

    def test_landauer_bound_is_positive_but_lower_bound_only(self):
        per_bit = landauer_bound(300.15)
        self.assertGreater(per_bit, 0.0)
        self.assertLess(per_bit, 1e-20)
        result = analyze_full_adder()
        self.assertGreater(result['landauer']['irreversible_adder_min_energy_joules'], 0.0)
        self.assertEqual(result['landauer']['reversible_adder_min_energy_joules'], 0.0)

    def test_gate_counts_depth_and_validation(self):
        circuit = full_adder_circuit()
        self.assertEqual(gate_counts(circuit), {'TOFFOLI': 2, 'CNOT': 2})
        self.assertEqual(circuit_depth(circuit, 4), 4)
        with self.assertRaises(ValueError):
            run_reversible([0, 0, 0, 0], [('BAD', 0)], 4)


if __name__ == '__main__':
    unittest.main()
