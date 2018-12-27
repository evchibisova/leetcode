import unittest
from task961 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty(self):
        self.assertIsNone(self.solution.repeatedNTimes([]))

    def test_from_leetcode_1(self):
        self.assertEqual(3, self.solution.repeatedNTimes([1, 2, 3, 3]))

    def test_from_leetcode_2(self):
        self.assertEqual(2, self.solution.repeatedNTimes([2,1,2,5,3,2]))

    def test_from_leetcode_3(self):
        self.assertEqual(5, self.solution.repeatedNTimes([5,1,5,2,5,3,5,4]))

