import unittest
from b_tree import b_tree_maker


class TestBTree(unittest.TestCase):
    def test_empty(self):
        self.assertIsNone(b_tree_maker([]))

    def test_ordinary_tree(self):
        tree_list = [10, 8, 12, 2, 9, 5, 13, None, 4]
        x = b_tree_maker(tree_list)
        self.assertEqual(tree_list, [x.val, x.left.val, x.right.val, x.left.left.val, x.left.right.val, x.right.left.val,
                                     x.right.right.val, x.left.left.left, x.left.left.right.val])
