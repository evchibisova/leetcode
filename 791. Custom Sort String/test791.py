import unittest
from task791 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual("abcd", self.s.customSortString("", "abcd"))
        self.assertEqual("", self.s.customSortString("cba", ""))

    def test_from_leetcode_1(self):
        self.assertCountEqual("cbad", self.s.customSortString("cba", "abcd"))