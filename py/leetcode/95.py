# Definition for a binary tree node.
class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def bulidTree(start,end):
            res=[]
            if start>end:
                res.append(None)
                return res
            if start==end:
                res.append(TreeNode(start))
                return res
            for i in range(start,end+1):
                leftNodes=bulidTree(start,i-1)
                rightNodes=bulidTree(i+1,end)
                for l in leftNodes:
                    for r in rightNodes:
                        root=TreeNode(i)
                        root.left=l
                        root.right=r
                        res.append(root)
            return res
        return bulidTree(1,n)

Solution().generateTrees(4)
