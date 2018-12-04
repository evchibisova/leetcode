import unittest
from task338 import Solution


class TestTask338(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_from_leetcode_1(self):
        self.assertEqual(self.solution.count_bits(2), [0, 1, 1])

    def test_from_leetcode_2(self):
        self.assertEqual(self.solution.count_bits(5), [0, 1, 1, 2, 1, 2])

    def test_zero(self):
        self.assertEqual(self.solution.count_bits(0), [0])

    def test_float(self):
        with self.assertRaises(TypeError):
            self.solution.count_bits(3.5)
