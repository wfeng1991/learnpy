# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.n=k
        self.r=0
        def help(root):
            if root:
                help(root.left)
                self.n-=1
                if self.n==0:
                    self.r=root.val
                help(root.right)
        help(root)
        return self.r
        