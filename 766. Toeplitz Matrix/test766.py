import unittest
from task766 import Solution

class TeatSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertIsNone(self.s.isToeplitzMatrix({}))

    def test_from_leetcode(self):
        self.assertTrue(self.s.isToeplitzMatrix([[1,2,3,4], [5,1,2,3], [9,5,1,2]]))

    def test_not_toeplitz(self):
        self.assertFalse(self.s.isToeplitzMatrix([[1,1,3,4], [5,1,2,3], [9,5,1,2]]))

