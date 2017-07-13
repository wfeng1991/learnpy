# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        def dfs(node,s,t):
            if node and node.left is None and node.right is None:
                if s+node.val==t:
                    return True
                else:
                    return False
            elif node:
                return dfs(node.left,s+node.val,t) or dfs(node.right,s+node.val,t)
            else:
                return False
        return dfs(root,0,sum)

