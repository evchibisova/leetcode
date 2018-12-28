import unittest
from task821 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        self.assertIsNone(self.solution.shortestToChar("", "a"))
        self.assertIsNone(self.solution.shortestToChar("abc", ""))

    def test_from_leetcode_1(self):
        self.assertEqual([3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0], self.solution.shortestToChar("loveleetcode", "e"))

    def test_char_not_in_string(self):
        with self.assertRaises(IndexError):
            self.solution.shortestToChar("abc", "d")
