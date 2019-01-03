import unittest
from b_tree import b_tree_maker  # take it from "Binary tree" folder
from task965 import Solution


class TestBTree(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def test_empty(self):
        self.assertTrue(self.s.isUnivalTree([]))

    def test_univalued_tree(self):
        x = b_tree_maker([1, 1, 1, 1, 1, None, 1])
        self.assertTrue(self.s.isUnivalTree(x))

    def test_not_univalued_tree(self):
        x = b_tree_maker([2,2,2,5,2])
        self.assertFalse(self.s.isUnivalTree(x))