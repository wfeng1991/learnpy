# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        pre,slow,fast=None,head,head
        while fast and fast.next:
            pre=slow
            slow=slow.next
            fast=fast.next.next
        pre.next=None

        node1=self.sortList(head)
        node2=self.sortList(slow)
        def merge(node1,node2):
            p=ListNode(0)
            r=p
            while node1 and node2:
                val1=node1.val
                val2=node2.val
                if val1>val2:
                    p.next=node2
                    node2=node2.next
                else:
                    p.next=node1
                    node1=node1.next
                p=p.next
            
            if node1:
                p.next=node1
            if node2:
                p.next=node2
            return r.next
        return merge(node1,node2)
    
