# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.r=[]
        def help(root):
            if not root:
                return
            self.r.append(root.val)
            help(root.left)
            help(root.right)  
        help(root)
        return self.r

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """ 
        r=[]
        stack=[]
        while root or stack:
            if root:
                while root:
                    r.append(root.val)
                    stack.append(root)
                    root=root.left
            else:
                if stack:
                    root=stack.pop().right
        return r
        
