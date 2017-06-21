# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        lst = []
        lst.append(root)
        res = []
        while len(lst)>0:
            t = []
            _lst = []
            for i in range(len(lst)-1,-1,-1):
                t.append(lst[i].val)
                if lst[i].left:
                    _lst.append(lst[i].left) 
                if lst[i].right:
                    _lst.append(lst[i].right) 
                lst.remove(lst[i])
            lst=_lst[::-1]
            res.append(t)
        return res[::-1]

t = TreeNode(3)

t.left = TreeNode(9)

t.right = TreeNode(20)

t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

print(Solution().levelOrderBottom(t))