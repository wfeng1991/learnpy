# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p=ListNode(0)
        t=p
        while p:
            pre_node=None
            _head=head
            while head and head.next and head.val==head.next.val:
                while _head:
                    pre_node=_head
                    _head=_head.next
                    if _head and _head.val==pre_node.val:
                        head=_head.next
                    else:
                        break
            p.next=head
            p=p.next
            if head:
                head=head.next
        return t.next
        
t=ListNode(1)
t.next=ListNode(2)
t.next.next=ListNode(2)
t.next.next.next=ListNode(3)
t.next.next.next.next=ListNode(3)
t.next.next.next.next.next=ListNode(5)
Solution().deleteDuplicates(t)