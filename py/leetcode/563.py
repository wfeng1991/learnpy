# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sum(root):
            if root is not None:
                return root.val + sum(root.left) + sum(root.right)
            else:
                return 0
        if root is not None:
            return abs(sum(root.left)-sum(root.right))+self.findTilt(root.left)+self.findTilt(root.right)
        else:
            return 0

t1=TreeNode(1)  
t1.left=TreeNode(2)
t1.right=TreeNode(3)
t1.left.left=TreeNode(4)
t1.right.left=TreeNode(5)


print(Solution().findTilt(t1))


            
