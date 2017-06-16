# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def eq(t1,t2):
            if t1 == t2:
                return True
            if t1 is not None and t2 is not None and t1.val == t2.val:
                return eq(t1.left, t2.left) and eq(t1.right, t2.right)
            else:
                return False
        if not eq(s,t):               
            return s is not None and (self.isSubtree(s.left,t) or self.isSubtree(s.right,t))
        else:
            return True

