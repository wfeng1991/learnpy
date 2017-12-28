# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p==root or q==root:
            return root
        self.path_p=[]
        self.path_q=[]
        def help(root,p,q,path):
            if root:
                if root==p:
                    self.path_p=path+[root]
                if root==q:
                    self.path_q=path+[root]
                if self.path_p and self.path_q:
                    return
                help(root.left,p,q,path+[root])
                help(root.right,p,q,path+[root])
        help(root,p,q,[])
        m=min(len(self.path_p),len(self.path_q))-1
        while m>=0 and self.path_p[m]!=self.path_q[m]:
            m-=1
        return self.path_p[m]
    
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root is None or p==root or q==root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is None:
            return right
        if right is None:
            return left
        return root

