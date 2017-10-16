# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res=[]
        if not root:
            return res
        q=[root]
        l2r=False
        res.append([root.val])
        v=[]
        tmp=[]
        while q:
            t=q[0]
            q=q[1:]
            if t.left:
                tmp.append(t.left)
                v.append(t.left.val)
            if t.right:
                tmp.append(t.right)
                v.append(t.right.val)
            if not q and tmp:
                q=tmp
                if l2r:
                    res.append(v)
                else:
                    res.append(v[::-1])
                v=[]
                tmp=[]
                l2r=not l2r
        return res
        
