"""
Unit tests for the sample NumPy program.
If NumPy is not available, the tests are skipped so the project remains import-safe.
"""

import unittest

try:
    import numpy as np
except Exception:
    np = None

import importlib

main = importlib.import_module('main')


@unittest.skipIf(np is None, "NumPy not installed; skipping numpy-dependent tests")
class TestNumpySample(unittest.TestCase):

    def test_create_linear_space(self):
        arr = main.create_linear_space(0, 2, 3)
        self.assertEqual(arr.shape, (3,))
        self.assertAlmostEqual(arr[0], 0.0)
        self.assertAlmostEqual(arr[-1], 2.0)

    def test_matrix_multiply(self):
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[2, 0], [1, 2]])
        C = main.matrix_multiply(A, B)
        expected = np.array([[4, 4], [10, 8]])
        np.testing.assert_allclose(C, expected)


if __name__ == '__main__':
    unittest.main()
