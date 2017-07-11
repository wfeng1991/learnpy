# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        self.r=[]
        def helper(node,nl):
            if node and node.left is None and node.right is None:
                s=''
                for n in nl:
                    s+=str(n.val)+'->'
                self.r.append(s+str(node.val))
            elif node:
                nl.append(node)
                helper(node.right,nl)                           
                helper(node.left,nl)
                nl.remove(node)
        helper(root,[])    
        return self.r
        
        

t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)
t.right.right=TreeNode(4)
t.right.left=TreeNode(2)

print(Solution().binaryTreePaths(t))