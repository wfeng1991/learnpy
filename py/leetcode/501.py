# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        d = dict()
        def helper(node,d):
            if node:
                if node.val in d:
                    d[node.val]+=1
                else:
                    d[node.val]=1
                helper(node.left,d)
                helper(node.right,d)
        helper(root,d)
        m=0
        for i in d:
            m=max(m,d[i])
        r=[]
        for i in d:
            if d[i]==m:
                r.append(i)
        return r

t=TreeNode(1)
t.right=TreeNode(2)
t.right.left=TreeNode(2)

print(Solution().findMode(t))
                
         

        
        