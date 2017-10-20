# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        def buildTree(arr):
            l=len(arr)
            if l>0:
                root=TreeNode(arr[l>>1])
                root.left=buildTree(arr[:l>>1])
                root.right=buildTree(arr[(l>>1)+1:])
                return root
        return buildTree(arr)