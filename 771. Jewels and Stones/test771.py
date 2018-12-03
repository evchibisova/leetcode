import unittest
from task771 import Solution


class TestTask771(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        self.assertEqual(self.solution.numJewelsInStones("", ""), 0)