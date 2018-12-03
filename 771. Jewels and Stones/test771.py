import unittest
from task771 import Solution


class TestTask771(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_from_leetcode_1(self):
        self.assertEqual(self.solution.numJewelsInStones("aA", "aAAbbbb"), 3)

    def test_from_leetcode_2(self):
        self.assertEqual(self.solution.numJewelsInStones("z", "ZZ"), 0)

    def test_all_jewels(self):
        self.assertEqual(self.solution.numJewelsInStones("z", "zzzzz"), 5)

    def test_empty_jewels(self):
        self.assertEqual(self.solution.numJewelsInStones("", "abcdef"), 0)

    def test_empty_stones(self):
        self.assertEqual(self.solution.numJewelsInStones("aA", ""), 0)

    def test_empty(self):
        self.assertEqual(self.solution.numJewelsInStones("", ""), 0)