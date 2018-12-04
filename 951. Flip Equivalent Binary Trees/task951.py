class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def __init__(self):
        self.flip_flag = True

    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right) \
               or self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)


# first_tree = TreeNode(1)
# first_tree.left = TreeNode(2)
# first_tree.left.left = TreeNode(4)
# first_tree.left.right = TreeNode(5)
# first_tree.left.right.left = TreeNode(7)
# first_tree.left.right.right = TreeNode(8)
# first_tree.right = TreeNode(3)
# first_tree.right.left = TreeNode(6)
#
# second_tree = TreeNode(1)
# second_tree.left = TreeNode(3)
# second_tree.left.right = TreeNode(6)
# second_tree.right = TreeNode(2)
# second_tree.right.left = TreeNode(4)
# second_tree.right.right = TreeNode(5)
# second_tree.right.right.left = TreeNode(8)
# second_tree.right.right.right = TreeNode(7)

# root1 = TreeNode(1)
# root2 = TreeNode(1)
# root1.left = TreeNode(1)
# root1.right = TreeNode(1)
# root2.left = TreeNode(2)
# root2.right = TreeNode(1)
#
# s = Solution()
# print(s.flipEquiv(root1, root2))