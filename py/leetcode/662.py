# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        start=[]
        end=[]
        def help(root,level,order,start,end):
            if root:
                if level==len(start):
                    start.append(order)
                    end.append(order)
                else:
                    end.insert(level,order)
                cur=end[level]-start[level]+1
                left=help(root.left,level+1,2*order,start,end)
                right=help(root.right,level+1,2*order+1,start,end)
                return max(cur,left,right)
            else:
                return 0
        return help(root,0,0,start,end)

