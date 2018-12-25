import unittest
from task806 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        self.assertIsNone(self.solution.numberOfLines([], "abc"))
        self.assertIsNone(self.solution.numberOfLines([10, 10, 10], ""))
        self.assertIsNone(self.solution.numberOfLines([], ""))

    def test_from_leetcode_1(self):
        self.assertEqual([3, 60], self.solution.numberOfLines([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                                                       "abcdefghijklmnopqrstuvwxyz"))
    def test_from_leetcode_2(self):
        self.assertEqual([2, 4], self.solution.numberOfLines([4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
                                                      "bbbcccdddaaa"))

    def test_tiny_widths_list(self):
        with self.assertRaises(IndexError):
            self.solution.numberOfLines([10], "az")

