# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        v=[root.val,1]
        q=[(root,1)]
        while len(q)>0:
            n=q[0][0]
            l=q[0][1]
            if l>v[1]:
                v=[n.val,l]
            if n.left:
                q.append((n.left,l+1))
                if l+1>v[1]:
                    v=[n.left.val,l+1]
            if n.right:
                q.append((n.right,l+1))
            del q[0]
        return v[0]

    # better solution
    def findBottomLeftValue1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        candidates = [root]
        while candidates:
            new_candidates = []
            for root in candidates:
                if root.left:
                    new_candidates.append(root.left)
                if root.right:
                    new_candidates.append(root.right)
            if not new_candidates:
                return candidates[0].val
            candidates = new_candidates