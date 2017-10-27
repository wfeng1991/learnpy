# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        pre=None
        cur=head
        while cur:
            _head=head
            if not pre:
                pre=cur
                cur=cur.next
            if cur.val<pre.val:
                pre.next=cur.next
                prenode=None
                while _head.val<cur.val:
                    prenode=_head
                    _head=_head.next
                if prenode:
                    prenode.next=cur
                    cur.next=_head
                else:
                    cur.next=_head
                    head=cur
            pre=cur
            cur=cur.next
        return head

h=ListNode(3)
h.next=ListNode(4)
h.next.next=ListNode(1)
Solution().insertionSortList(h)

                
                
                