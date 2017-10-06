# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res=[]
        def help(root,t,res):
            if root:
                if root.left is None and root.right is None:
                    res.append(t*10+root.val)
                else:
                    help(root.left,t*10+root.val,res)
                    help(root.right,t*10+root.val,res)
        help(root,0,res)
        return sum(res)