# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        self.val=[]
        def sum(node):
            if not node:
                return 0
            v = node.val + sum(node.left) + sum(node.right)
            self.val.append(v)
            return v
        sum(root)
        dic = dict()
        for n in self.val:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        r=[]
        m = max(dic.values())
        for k in dic:
            if dic[k]==m:
                r.append(k)
        return r