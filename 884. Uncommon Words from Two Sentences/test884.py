import unittest
from task884 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty_input_list(self):
        self.assertEqual([], self.s.uncommonFromSentences("", ""))
        self.assertEqual(["apple"], self.s.uncommonFromSentences("apple", ""))
        self.assertEqual(["banana"], self.s.uncommonFromSentences("", "banana"))

    def test_empty_result(self):
        self.assertEqual([], self.s.uncommonFromSentences("apple", "apple"))

    def test_from_leetcode_1(self):
        self.assertEqual(["sweet","sour"], self.s.uncommonFromSentences("this apple is sweet", "this apple is sour"))

    def test_from_leetcode_2(self):
        self.assertEqual(["banana"], self.s.uncommonFromSentences("apple apple", "banana"))

    def test_from_leetcode_3(self):
        self.assertEqual(["ejt"], self.s.uncommonFromSentences("s z z z s", "s z ejt"))