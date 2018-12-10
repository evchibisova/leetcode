import unittest
from task807 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            self.assertEqual(0, self.s.maxIncreaseKeepingSkyline([]))

    def test_empty_row(self):
        self.assertEqual(0, self.s.maxIncreaseKeepingSkyline([[]]))

    def test_from_leetcode_1(self):
        self.assertEqual(35, self.s.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))