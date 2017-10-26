# Definition for binary tree with next pointer.
class TreeLinkNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing

    def connect(self, root):
        lastCur = root
        pre = None
        cur = None
        lst = None
        while lastCur:
            cur = lastCur
            while cur:
                if cur.left:
                    if not lst:
                        lst = cur.left
                        pre = lst
                    else:
                        pre.next = cur.left
                        pre = pre.next
                if cur.right:
                    if not lst:
                        lst = cur.right
                        pre = lst
                    else:
                        pre.next = cur.right
                        pre = pre.next
                cur=cur.next
            lastCur = lst
            pre = None
            cur = None
            lst = None

t=TreeLinkNode(1)
Solution().connect(t)
