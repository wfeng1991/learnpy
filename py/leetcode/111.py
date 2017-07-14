# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.m=-1
        def deep(node,d):
            if node and node.left is None and node.right is None:
                self.m=min(self.m,d+1) if self.m!=-1 else d+1
            elif node:
                deep(node.left,d+1)
                deep(node.right,d+1)
        deep(root, 0)
        return self.m

        

        