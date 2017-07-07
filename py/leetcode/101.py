# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def helper(left,right):
            if left and right:
                return  left.val==right.val and helper(left.left,right.right) and helper(left.right,right.left)
            elif left==right:
                return True
            else:
                return False
        
        if root:
            return helper(root.left,root.right)
        else:
            return True



