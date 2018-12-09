import unittest
from task811 import Solution

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertEqual([], self.s.subdomainVisits([]))

    def test_from_leetcode_1(self):
        self.assertEqual(["9001 discuss.leetcode.com", "9001 leetcode.com", "9001 com"].sort(),
                         self.s.subdomainVisits(["9001 discuss.leetcode.com"]).sort())

    def test_from_leetcode_2(self):
        self.assertEqual(["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"].sort(),
                         self.s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]).sort())