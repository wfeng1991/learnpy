# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        res=[]
        def preorder(root,dic,res):
            if root:
                s=str(root.val)+preorder(root.left,dic,res)+preorder(root.right,dic,res)
                dic[s]=dic.get(s,0)+1
                if dic[s]==2:
                    res.append(root)
                return s
            else:
                return "#"
        preorder(root,{},res)
        return res
