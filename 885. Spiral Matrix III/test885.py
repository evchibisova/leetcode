import unittest
from task885 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual([], self.s.spiralMatrixIII(0, 0, 0, 0), msg="must return an empty list")

    def test_from_leetcode_1(self):
        answer = [[0,0],[0,1],[0,2],[0,3]]
        self.assertEqual(answer, self.s.spiralMatrixIII(1, 4, 0, 0))

    def test_from_leetcode_2(self):
        answer = [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],
             [3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],
             [0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
        self.assertEqual(answer, self.s.spiralMatrixIII(5, 6, 1, 4))