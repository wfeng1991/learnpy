# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 中序遍历
        l=[]
        self.b(root,l)
        m = -1
        i=1
        while i<len(l):
            if m==-1:
                m=l[i]-l[i-1]
            else:
                m=min(m,l[i]-l[i-1])
            i+=1
        return m

    
    def b(self,root,l):
        if root is not None:
            self.b(root.left,l)
            l.append(root.val)
            self.b(root.right,l)


t = TreeNode(1)
t.right = TreeNode(3)
t.right.left = TreeNode(2)
l=[]
Solution().b(t,l)
print(l)

        
        
             

    
