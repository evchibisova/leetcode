class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        flag = True
        if not root:
            return True
        if root.left:
            flag = root.left.val == root.val
        if flag and root.right:
            flag = root.right.val == root.val
        return flag and self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
