# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        _head=ListNode(-float('inf'))
        _head.next=head
        cur=_head.next
        start=pre=_head
        while cur:
            if cur.val<x:
                if start.next==cur:
                    start=start.next
                else:
                    pre.next=cur.next
                    n=start.next
                    start.next=cur
                    cur.next=n
                    start=cur
            pre=cur
            cur=cur.next
        return _head.next

t=ListNode(2)
t.next=ListNode(1)
Solution().partition(t,2)        