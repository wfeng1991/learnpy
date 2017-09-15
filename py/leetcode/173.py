# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root=root
        self.stack=[]
        self.cur_node=root
        

    def hasNext(self):
        """
        :rtype: bool
        """
        node=self.cur_node
        while node:
            self.stack.append(node)
            curNode = node
            node=node.left
        return len(self.stack)!=0

    def next(self):
        """
        :rtype: int
        """
        v = None
        if self.stack:
            n = self.stack.pop()
            v = n.val
            if n.right:
                self.cur_node = n.right
            else:
                self.cur_node = None
        else:
            self.cur_node = None
        return v
        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())