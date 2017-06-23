# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        dic = dict()
        dic[0]=1
        def helper(node, presum, sum, dic):
            if not node:
                return 0
            presum += node.val
            res = dic[presum-sum] if presum-sum in dic else 0
            if presum in dic:
                dic[presum]+=1
            else:
                dic[presum]=1
            res += helper(node.right, presum, sum, dic)+helper(node.left, presum, sum, dic)
            dic[presum]-=1
            return res
        return helper(root, 0, sum, dic)
        
        


t = TreeNode(10)

t.left = TreeNode(5)

t.right = TreeNode(-3)

t.right.right = TreeNode(11)

t.left.left = TreeNode(3)
t.left.right = TreeNode(2)

t.left.left.left = TreeNode(3)
t.left.left.right = TreeNode(-2)

t.left.right.right = TreeNode(1)

print(Solution().pathSum(t,8))