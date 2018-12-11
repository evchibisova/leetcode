import unittest
from task557 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual("", self.s.reverseWords(""))

    def test_from_leetcode_1(self):
        self.assertEqual("s'teL ekat edoCteeL tsetnoc", self.s.reverseWords("Let's take LeetCode contest"))

    def test_inp_is_not_a_string(self):
        with self.assertRaises(AttributeError, msg="input is not a string"):
            self.s.reverseWords(1)
            self.s.reverseWords(1.0)
            self.s.reverseWords([1, 2, 3])
