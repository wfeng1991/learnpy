# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd1(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        self.cnt=0
        def help(head,n,l):
            if head:
                help(head.next,n,l+1)
            else:
                self.cnt=l
            if self.cnt and self.cnt-n-1==l:
                head.next=head.next.next
        help(head,n,0)
        if self.cnt==n:
            return head.next
        else:
            return head
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(-1)
        start.next = head
        fast = start
        slow = start
        for _ in range(n):
            fast = fast.next
        while fast.next != None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return start.next
        

t=ListNode(1)
t.next=ListNode(2)
print(Solution().removeNthFromEnd(t,1))
        