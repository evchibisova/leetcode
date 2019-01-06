import unittest
from task868 import Solution


class TestTask868(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_float(self):
        for i in [10.5, "abc", "123"]:
            with self.subTest(case=i):
                self.assertRaises(TypeError, self.s.binaryGap, i)

    def test_just_one_one(self):
        for i in range(10):
            with self.subTest(case=i):
                self.assertEqual(0, self.s.binaryGap(2**i))

    def test_zero(self):
        self.assertEqual(0, self.s.binaryGap(0))

    def test_leetcode_cases(self):
        cases = [22, 5, 6]
        answers = [2, 2, 1]
        for i in range(len(cases)):
            with self.subTest(case=i):
                self.assertEqual(answers[i], self.s.binaryGap(cases[i]))
