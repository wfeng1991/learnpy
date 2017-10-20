# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, s):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def help(root,t,s,res):
            if root and not root.left and not root.right:
                if root.val==s:
                    res.append(t+[root.val])
            elif root:
                help(root.left,t+[root.val],s-root.val,res)
                help(root.right,t+[root.val],s-root.val,res)
            else:
                return
        res=[]
        help(root,[],s,res)
        return res

        