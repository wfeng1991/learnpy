# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def deleteNode1(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        _root=TreeNode(None)
        _root.left=root
        def help(root,key):
            if root:
                p=[0,None]
                if root.left and root.left.val==key:
                    p=[1,root.left]
                if root.right and root.right.val==key:
                    p=[2,root.right]
                if p[0]:
                    left=p[1].left
                    right=p[1].right
                    if left is None:
                        p[1]=right
                    elif right is None:
                        p[1]=left
                    else:
                        _right=left.right
                        left.right=right
                        pre=right
                        t=right.left 
                        while t:
                            pre=t
                            t=t.left
                        pre.left=_right
                        p[1]=left
                    if p[0]==1:
                        root.left=p[1]
                    elif p[0]==2:
                        root.right=p[1]
                else:
                    help(root.left,key)
                    help(root.right,key)
        help(_root,key)
        return _root.left

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def getMax(node):
            while node.right:
                node=node.right
            return node
        def deleteNode(root,key):
            if root is None:
                return None
            if root.val>key:
                root.left=deleteNode(root.left,key)
            elif root.val<key:
                root.right=deleteNode(root.right,key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    _max=getMax(root.left)
                    root.val=_max.val
                    root.left=deleteNode(root.left,root.val)
            return root
        return deleteNode(root, key)

                


root=TreeNode(5)
root.left=TreeNode(3)
root.left.right=TreeNode(4)
root.left.left=TreeNode(2)
root.right=TreeNode(6)
root.right.right=TreeNode(7)

Solution().deleteNode(root,3)

        
