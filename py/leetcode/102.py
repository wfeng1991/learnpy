# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        r=[]
        q=[root]
        while q:
            _q=[]
            _r=[]
            while q:
                n=q[0]
                q=q[1:]
                _r.append(n.val)
                if n.left:
                    _q.append(n.left)
                if n.right:
                    _q.append(n.right)
            if _q:
                q=_q
            if _r:
                r.append(_r)
        return r
