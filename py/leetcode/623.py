# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d==1:
            r=TreeNode(v)
            r.left=root
            return r
        q=[root]
        deep=0
        t=[]
        while q:
            n = q.pop()
            if not n.left and deep==d-1:
                n.left=TreeNode(v)
            elif n.left and deep==d-1:
                tmp = n.left
                n.left=TreeNode(v)
                n.left.left=tmp
            elif n.left:
                t.append(n.left)

            if not n.right and deep==d-1:
                n.right=TreeNode(v)    
            elif n.right and deep==d-1:
                tmp = n.right
                n.right=TreeNode(v)
                n.right.right=tmp
            elif n.right:
                t.append(n.right)
            if not q and t and deep<d-1:
                deep+=1
                q=t
                t=[]
        return root
            
