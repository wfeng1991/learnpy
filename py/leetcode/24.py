# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        h=None
        pre=None
        cur=head
        while cur:
            nt=cur.next
            if nt:
                cur.next=nt.next
                nt.next=cur
                if pre:
                    pre.next=nt
            pre=cur
            cur=cur.next
            if h is None:
                h=nt
        return h
        
t=ListNode(1)
t.next=ListNode(2)
t.next.next=ListNode(3)
# t.next.next.next=ListNode(4)
Solution().swapPairs(t)        