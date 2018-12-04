import unittest
from task771 import Solution


class TestTask771(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_from_leetcode_1(self):
        self.assertEqual(self.solution.numJewelsInStones("aA", "aAAbbbb"), 3)