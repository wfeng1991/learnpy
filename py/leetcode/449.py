# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.s=''
        q=[root]
        while q:
            t=q[0]
            q=q[1:]
            if t:
                self.s+=str(t.val)+'#'
                q.append(t.left)
                q.append(t.right)
            else:
                self.s+='n#'
        return self.s[:-1]


        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        d=data.split('#')
        root=None
        q=[]
        if d[0].isdigit():
            root=TreeNode(int(d[0]))
            d=d[1:]
            q.append(root)
        else:
            return root
        while q and d:
            t=q[0]
            q=q[1:]
            if t:
                if d[0].isdigit():
                    t.left=TreeNode(int(d[0]))
                    q.append(t.left)
                if d[1].isdigit():
                    t.right=TreeNode(int(d[1]))
                    q.append(t.right)
                d=d[2:]
        return root
            
                
        

# Your Codec object will be instantiated and called as such:
codec = Codec()
root=TreeNode(5)
root.left=TreeNode(3)
root.right=TreeNode(6)
# root.left.left=TreeNode(2)
# root.left.right=TreeNode(4)
# root.left.left.left=TreeNode(1)
t=codec.deserialize(codec.serialize(root))

t