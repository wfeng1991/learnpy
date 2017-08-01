# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        t=[root]
        minval=None
        r=[]
        tmp=[]
        while t:
            n=t.pop()
            if not minval or n.val>minval:
                minval=n.val
            if n.left:
                tmp.append(n.left)
            if n.right:
                tmp.append(n.right)
            if not t:
                t=tmp
                r.append(minval)
                minval=None
                tmp=[]
        return r
        