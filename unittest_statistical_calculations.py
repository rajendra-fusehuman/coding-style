import numpy as np
import unittest

def mean_median_std(numbers: list) -> tuple:
    """
    Calculates mean, median and standard deviation of provided numbers.

    Parameters
    ----------
    number : list
        list of numbers to calculate statistical parameters

    Returns
    -------
    Tuple
        Returns tuple of calculated mean, median and standard deviation
    """
    if len(numbers) == 0:
        raise ValueError("Given list is empty")

    mean = round(np.mean(numbers), 3)
    median = round(np.median(numbers), 3)
    std = round(np.std(numbers), 3)

    return mean, median, std


class TestStatisticalCalculations(unittest.TestCase):
    """Defines test methods to validate statistical calculations"""
    def test_empty_list(self):
        with self.assertRaises(ValueError):
            mean_median_std([])

    def test_single_element(self):
        data = [10]
        self.assertEqual(mean_median_std(data), (10.0, 10, 0.0))

    def test_multiple_elements(self):
        data = [1, 2, 3, 4, 5]
        self.assertAlmostEqual(mean_median_std(data), (3.0, 3, 1.414))
        data = [-2, -1, 0, 1, 2]
        self.assertEqual(mean_median_std(data), (0, 0, 1.414))


if __name__ == "__main__":
    unittest.main()
