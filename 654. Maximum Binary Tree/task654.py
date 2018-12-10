class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        max_el = max(nums)
        tree = TreeNode(max_el)
        tree.left = self.constructMaximumBinaryTree(nums[:nums.index(max_el)])
        tree.right = self.constructMaximumBinaryTree(nums[nums.index(max_el)+1:])
        return tree

s = Solution()
print(s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5]))