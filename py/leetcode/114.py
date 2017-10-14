# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def help(root):
            if root:
                left=help(root.left)
                right=help(root.right)
                if left: 
                    root.right=left
                    root.left=None
                    while left.right:
                        left=left.right
                    left.right=right
                return root
            else:
                return None
        help(root)

t=TreeNode(1)
t.right=TreeNode(2)
Solution().flatten(t)

        