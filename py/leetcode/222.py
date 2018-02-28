# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        i=0
        curLevel=[root]
        lastLvCnt=0
        while curLevel:
            lastLvCnt=len(curLevel)
            _curLevel=[]
            while curLevel:
                t=curLevel.pop(0)
                if t.left:
                    _curLevel.append(t.left)
                if t.right:
                    _curLevel.append(t.right)
            curLevel=_curLevel
            i+=1
        return 1 if i==1 else pow(2,i-1)-1+lastLvCnt

    def countNodes1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import math
        if root == None:
            return 0
        
        left = root
        right = root
        height = 0
        
        while(right):
            left = left.left
            right = right.right
            height +=1
        
        if left==None:
            return int(math.pow(2,height) -1)
        
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

t=TreeNode(1)
t.left=TreeNode(2)
t.right=TreeNode(3)

print(Solution().countNodes(t))
        
        