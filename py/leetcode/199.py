# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        r=[]
        if not root:
            return r
        q=[root]
        while q:
            r.append(q[-1].val)
            _q=[]
            while q:
                t=q[0]
                q=q[1:]
                if t.left:
                    _q.append(t.left)
                if t.right:
                    _q.append(t.right)
            if _q:
                q=_q
        return r
            

