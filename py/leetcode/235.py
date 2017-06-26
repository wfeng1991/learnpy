# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def dfs(root,p):
            if not root:
                return False
            if root==p:
                return True
            return dfs(root.left, p) or dfs(root.right, p)
        if not root:
            return
        if dfs(root,p) and dfs(root,q):
            node = root
            n1 = self.lowestCommonAncestor(root.left,p,q) 
            n2 = self.lowestCommonAncestor(root.right,p,q)
            if n1:
                node = n1
            if n2:
                node = n2
            return node
        
        
        

            