import unittest
import numpy as np
from armendariz_main import Distributions, NumpyDistribution


class TestDistributions(unittest.TestCase):
    def test_normal_distribution(self):
        dist = Distributions("normal", 0, 1, 1000)
        self.assertEqual(dist.distribution, "normal")
        self.assertEqual(len(dist.get_data()), 1000)

    def test_invalid_distribution(self):
        with self.assertRaises(ValueError):
            Distributions("Invalid", 0, 1, 1000)


class TestNumpyDistribution(unittest.TestCase):
    def test_lognormal_distribution(self):
        dist = NumpyDistribution("lognormal", 1, 0.5, 1000)
        self.assertEqual(dist.distribution, "lognormal")
        self.assertEqual(len(dist.get_data()), 1000)

    def test_laplace_distribution(self):
        dist = NumpyDistribution("laplace", 0, 1, 500)
        self.assertEqual(dist.distribution, "laplace")
        self.assertEqual(len(dist.get_data()), 500)

    def test_invalid_distribution(self):
        with self.assertRaises(ValueError):
            NumpyDistribution("Invalid", 0, 1, 1000)


if __name__ == "__main__":
    unittest.main()
