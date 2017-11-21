# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def help(inorder,postorder):
            if inorder:
                idx=inorder.index(postorder.pop())
                root=TreeNode(inorder[idx])
                root.right=help(inorder[idx+1:],postorder)
                root.left=help(inorder[:idx],postorder)
                return root
        return help(inorder,postorder)

print(Solution().buildTree([1,2,3,4],[1,4,3,2]))
