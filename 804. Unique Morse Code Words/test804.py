import unittest
from task804 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(0, self.s.uniqueMorseRepresentations([]))

    def test_from_leetcode(self):
        self.assertEqual(2, self.s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

    def test_code_tables(self):
        """what if we have another code table, not Unicode?"""
        pass