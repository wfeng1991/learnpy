# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val > l2.val:
            t = l2
            l2 = l2.next
        else:
            t = l1
            l1 = l1.next
        h = t
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                t.next = l2
                l2 = l2.next
            else:
                t.next = l1
                l1 = l1.next
            t = t.next
        if l1 is not None:
            t.next = l1
        if l2 is not None:
            t.next = l2      
        return h


l1 = ListNode(-7)


# [-10,-10,-9,-4,1,6,6]
l2 = ListNode(-10)
tt = ListNode(-10)
l2.next = tt
t2 = l2.next 
tt = ListNode(-9)
t2.next = tt

t2 = t2.next 
tt = ListNode(-4)
t2.next = tt

t2 = t2.next 
tt = ListNode(-1)
t2.next = tt

t2 = t2.next 
tt = ListNode(6)
t2.next = tt

t2 = t2.next 
tt = ListNode(6)
t2.next = tt

s=Solution()
s = s.mergeTwoLists(l1, l2)
while s is not None:
    print(s.val)
    s = s.next
