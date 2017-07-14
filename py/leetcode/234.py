# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome1(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        self.h=head
        def travel(tail):
            if tail.next:
                t = travel(tail.next)
                self.h=self.h.next
                return t and self.h.val==tail.val
            else:
                return self.h.val==tail.val
        return travel(head)

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        r = []
        t=head
        while t:
            r.append(t)
            t=t.next
        i=0
        while i<len(r)//2:
            if r[i].val!=r[-1-i].val:
               return False
            i+=1
        return True

                
t1=ListNode(1)
t1.next=ListNode(3)
t1.next.next=ListNode(2)
t1.next.next.next=ListNode(2)
t1.next.next.next.next=ListNode(3)
t1.next.next.next.next.next=ListNode(1)
print(Solution().isPalindrome1(t1))
        