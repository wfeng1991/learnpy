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
    def connect1(self, root):
        if root is None:
            return
        q=[root]
        t=[]
        while q:
            p=q[0]
            q=q[1:]
            if p.left:
                t.append(p.left)
            if p.right:
                t.append(p.right)
            if len(q)==0 and t:
                q=t
                t=[]
                i=0
                while i<len(q)-1:
                    q[i].next=q[i+1]
                    i+=1
    
    def connect(self, root):
        if not root:
            return
        while(root.left):
            p = root
            while(p):
                p.left.next = p.right
                if p.next:
                    p.right.next = p.next.left
                p = p.next
            root = root.left

t=TreeLinkNode(1)
t.left=TreeLinkNode(2)
t.right=TreeLinkNode(3)
Solution().connect(t)
        
        
