import unittest
from task463 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertIsNone(self.s.islandPerimeter([]))

    def test_simple_maps(self):
        maps = [[[0, 0, 0, 0],[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]],
                [[1, 1, 1, 0], [1, 0, 1, 0], [1, 0, 0, 0], [1, 1, 0, 0]],
                [[0, 0, 0, 1], [0, 1, 0, 1], [0, 0, 0, 1]],
                [[0, 1, 1], [0, 0, 0], [1, 1, 0]]]
        perimeters = [8, 18, 12, 12]
        for i in range(len(maps)):
            with self.subTest(case = maps[i]):
                self.assertEqual(perimeters[i], self.s.islandPerimeter(maps[i]))

    def test_from_leetcode(self):
        self.assertEqual(16, self.s.islandPerimeter([[0,1,0,0],
                                                     [1,1,1,0],
                                                     [0,1,0,0],
                                                     [1,1,0,0]]))

    def test_fool_maps(self):
        maps = [[[1]],
                [[1, 1], [1, 1]],
                [[1, 1, 1]],
                [[1], [1], [1]]]
        perimeters = [4, 8, 8, 8]
        for i in range(len(maps)):
            with self.subTest(case = maps[i]):
                self.assertEqual(perimeters[i], self.s.islandPerimeter(maps[i]))
