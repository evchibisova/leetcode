import unittest
from task500 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual(self.s.findWords([]), [])

    def test_from_leetcode_1(self):
        self.assertEqual(self.s.findWords(["Hello", "Alaska", "Dad", "Peace"]), ["Alaska", "Dad"])

    def test_all_strings_in_rows(self):
        self.assertEqual(self.s.findWords(["Alaska", "Dad"]), ["Alaska", "Dad"])

    def no_strings_in_rows(self):
        self.assertEqual(self.s.findWords(["Hello", "Peace"]), [])
        self.assertEqual(self.s.findWords(["Alaska1", "Dad2"]), [])
