__author__ = 'kochanik'

import random
import unittest
from quicksort import _partition, quicksort


class TestQuicksort(unittest.TestCase):

    def setUp(self):
        self.mass = [random.randint(1, 100) for _ in range(4)]

    def test_qsort(self):
        lastindex = len(self.mass) - 1
        quick = quicksort(self.mass, 0, lastindex)
        self.assertEqual(quick, sorted(self.mass))

    def test_empty(self):
        with self.assertRaises(ValueError):
                quicksort(list(), 0, 0)

    def test_over(self):
        with self.assertRaises(ValueError):
            quick = quicksort(self.mass, 0, 100000)

    def test_negative(self):
        with self.assertRaises(ValueError):
            quick = quicksort(self.mass, -1, 100000)


class TestPartition(unittest.TestCase):

    def test_partition(self):
        arr = [4, 5]
        res = list(arr)
        _partition(res, 0, len(arr)-1)
        self.assertEqual(res, [4, 5])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            _partition(1, 0, 0)


if __name__ == '__main__':
    unittest.main()
