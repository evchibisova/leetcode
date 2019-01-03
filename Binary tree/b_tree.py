class TreeNode(object):
    """Definition for a binary tree node."""
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def b_tree_maker(roots):
    """make binary tree from list of values"""
    lst = roots.copy()
    if not lst:
        return None
    tree = TreeNode(lst.pop(0))
    root_list = [tree]
    while root_list:
        root = root_list.pop(0)
        if lst:
            root.left = TreeNode(lst.pop(0))
            root_list.append(root.left)
        if lst:
            root.right = TreeNode(lst.pop(0))
            root_list.append(root.right)

    return tree

# x = b_tree_maker([10, 8, 12, 2, 9, 5, 13, None, 4])
# print(x.val, x.left.val, x.right.val, x.left.left.val, x.left.right.val, x.right.left.val, x.right.right.val,
#       x.left.left.left.val, x.left.left.right.val)
