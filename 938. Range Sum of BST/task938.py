class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        root_sum = 0
        if not root:
            return 0
        if L <= root.val <= R:
            root_sum += root.val
        if root.val > L:
            root_sum += self.rangeSumBST(root.left, L, R)
        if root.val < R:
            root_sum += self.rangeSumBST(root.right, L, R)
        return root_sum

root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right = TreeNode(15)
root.right.left = None
root.right.right = TreeNode(18)

s = Solution()
print(s.rangeSumBST(root, 7, 15))