import unittest
from task893 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(0, self.s.numSpecialEquivGroups([]))

    def test_from_leetcode_1(self):
        self.assertEqual(3, self.s.numSpecialEquivGroups(["a", "b", "c", "a", "c", "c"]))

    def test_from_leetcode_2(self):
        self.assertEqual(4, self.s.numSpecialEquivGroups(["aa", "bb", "ab", "ba"]))

    def test_from_leetcode_3(self):
        self.assertEqual(3, self.s.numSpecialEquivGroups(["abc", "acb", "bac", "bca", "cab", "cba"]))

    def test_from_leetcode_4(self):
        self.assertEqual(1, self.s.numSpecialEquivGroups(["abcd", "cdab", "adcb", "cbad"]))

    def test_all_strings_diff(self):
        self.assertEqual(4, self.s.numSpecialEquivGroups(["a", "b", "c", "d"]))
