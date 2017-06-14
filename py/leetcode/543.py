# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        def maxdeep(root, maxd = 0):
            if root is None:
                return 0, maxd
            left, maxd = maxdeep(root.left, maxd)
            right, maxd = maxdeep(root.right, maxd)
            maxd = max(maxd, left+right)
            return max(left, right)+1, maxd
        v, maxd = maxdeep(root)
        return maxd
        

t1 = TreeNode(1)
t1.left=TreeNode(2)
t1.right=TreeNode(3)
t1.left.left=TreeNode(4)
t1.left.right=TreeNode(5)
t1.left.right.left=TreeNode(5)

print(Solution().diameterOfBinaryTree(t1))
    
        