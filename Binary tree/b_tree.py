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
            if lst[0]:
                root.left = TreeNode(lst.pop(0))
            else:
                lst.pop(0)
            root_list.append(root.left)
        if lst:
            if lst[0]:
                root.right = TreeNode(lst.pop(0))
            else:
                lst.pop(0)
            root_list.append(root.right)

    return tree
