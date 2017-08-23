# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.mem={}
        def help(root, rob):
            if root and not root.left and not root.right:
                if rob:
                    return root.val
                else:
                    return 0
            elif root:
                if (root,1,0) in self.mem:
                    t1=self.mem[(root,1,0)]
                else:
                    t1=help(root.left, False)
                    self.mem[(root,1,0)]=t1
                if (root,2,0) in self.mem:
                    t2=self.mem[(root,2,0)]
                else:
                    t2=help(root.right, False)
                    self.mem[(root,2,0)]=t2
                if rob:
                    return root.val+t1+t2
                else:
                    if (root,1,1) in self.mem:
                        t3=self.mem[(root,1,1)]
                    else:
                        t3=help(root.left, True)
                        self.mem[(root,1,1)]=t3
                    if (root,2,1) in self.mem:
                        t4=self.mem[(root,2,1)]
                    else:
                        t4=help(root.right, True)
                        self.mem[(root,2,1)]=t2
                    return max(t3+t4,t3+t2,t1+t4,t1+t2)
            else:
                return 0
        return max(help(root,True), help(root,False))