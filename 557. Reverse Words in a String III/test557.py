import unittest
from task557 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual("", self.s.reverseWords(""))

    def test_from_leetcode_1(self):
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", self.s.reverseWords("Let's take LeetCode contest"))

    def test_is_integer(self):
        with self.assertRaises(AttributeError, msg="it's a number, not a string"):
            self.s.reverseWords(1)

    def test_is_list(self):
        with self.assertRaises(AttributeError, msg="it's a number, not a string"):
            self.s.reverseWords([1,2,3])