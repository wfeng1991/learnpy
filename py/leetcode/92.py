# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m==n:
            return head
        i=1
        pointer=head
        start=None
        while pointer:
            if m==i:
                break
            start=pointer
            i+=1
            pointer=pointer.next
        cur=pointer
        pre=start
        while i<=n:
            nxt=cur.next
            cur.next=pre
            pre=cur
            cur=nxt
            i+=1
        if pointer!=cur:
            pointer.next=cur
        if start:
            start.next=pre
            return head
        else:
            return pre
t=ListNode(5)
t.next=ListNode(3)
Solution().reverseBetween(t,1,2)
            
