# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten1(self, root):
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

    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        def dfs(root):            
            if not root.right and not root.left:
                return root
            right = root.right
            right_last, left_last = None, None
            if root.right:
                right_last = dfs(root.right)
            if root.left:
                left_last = dfs(root.left)
                root.right = root.left
                root.left = None
                left_last.right = right
                right = root.right
            return right_last or left_last
        if root:dfs(root)


t=TreeNode(1)
t.right=TreeNode(2)
Solution().flatten(t)

        