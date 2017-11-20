# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree1(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        seg=inorder.index(preorder[0])
        inleft=inorder[:seg]
        inright=inorder[seg+1:]
        preorder=preorder[1:]
        preleft=preorder[:len(inleft)]
        preright=preorder[len(inleft):]
        def help(root,inleft,inright,preleft,preright):
            if preleft:
                root.left=TreeNode(preleft[0])
                t1=preleft[0]
                preleft=preleft[1:]
                seg1=inleft.index(t1)
                inleft1=inleft[:seg1]
                inright1=inleft[seg1+1:]
                preleft1=preleft[:len(inleft1)]
                preright1=preleft[len(inleft1):]
                help(root.left,inleft1,inright1,preleft1,preright1)
            if preright:
                root.right=TreeNode(preright[0])
                t2=preright[0]
                preright=preright[1:]
                seg2=inright.index(t2)
                inleft2=inright[:seg2]
                inright2=inright[seg2+1:]
                preleft2=preright[:len(inleft2)]
                preright2=preright[len(inleft2):]
                help(root.right,inleft2,inright2,preleft2,preright2)
        help(root,inleft,inright,preleft,preright)
        return root

    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
    
Solution().buildTree([1,2,3,4], [1,2,3,4])