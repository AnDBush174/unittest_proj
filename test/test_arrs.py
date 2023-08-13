import doctest
import unittest
from utils import arrs

class ArrsTestCase(unittest.TestCase):
    def test_get_existing_index(self):
        """
        Протестируйте функцию get() с существующим индексом.
        """
        result = arrs.get([1, 2, 3], 1, "test")
        self.assertEqual(result, 2)

    def test_get_nonexisting_index(self):
        """
        Протестируйте функцию get() с существующим индексом.
        """
        result = arrs.get([], 0, "test")
        self.assertEqual(result, "test")

    def test_get_out_of_bounds_index(self):
        """
        Протестируйте функцию get() с выходом за пределы индекса.
        """
        result = arrs.get(["a", "b", "c"], 5, None)
        self.assertIsNone(result)

    def test_get_negative_index(self):
        """
        Протестируйте функцию get() с отрицательным индексом.
        """
        result = arrs.get(["x", "y", "z"], -1, "default")
        self.assertEqual(result, "z")

    def test_slice(self):
        """
        Протестируйте функцию my_slice() в разных случаях.
        """
        result = arrs.my_slice([1, 2, 3, 4], 1, 3)
        self.assertEqual(result, [2, 3])

        result = arrs.my_slice([1, 2, 3], 1)
        self.assertEqual(result, [2, 3])

        result = arrs.my_slice([1, 2, 3, 4, 5], -3, -1)
        self.assertEqual(result, [3, 4])

        result = arrs.my_slice([], 0, 2)
        self.assertEqual(result, [])

        result = arrs.my_slice(["a", "b", "c", "d"], 0, -1)
        self.assertEqual(result, ["a", "b", "c"])

        result = arrs.my_slice([1, 2, 3, 4, 5], -1)
        self.assertEqual(result, [5])

    def test_empty_slice(self):
        """
        Протестируйте функцию my_slice() с пустым списком.
        """
        result = arrs.my_slice([], 0, 2)
        self.assertEqual(result, [])

    def suite(self):
        """
        Определить набор тестов.
        """
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(ArrsTestCase))
        return suite


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(ArrsTestCase().suite())


