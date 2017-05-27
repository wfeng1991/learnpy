# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = 0
        if root is None:
            return res
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                res+=root.left.val
            else:
                res+=self.sumOfLeftLeaves(root.left)
        res += self.sumOfLeftLeaves(root.right)
        return res
        
        
# [3,9,20,null,null,15,7]
t1=TreeNode(3)
t1.left=TreeNode(9)
t1.right=TreeNode(20)
t1.right.left=TreeNode(15)
t1.right.right=TreeNode(7)

print(Solution().sumOfLeftLeaves(t1))