# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        la,lb=0,0
        na,nb=headA,headB
        ta,tb=headA,headB
        while na:
            la+=1
            ta=na
            na=na.next
        while nb:
            lb+=1
            tb=nb
            nb=nb.next
        if ta!=tb:
            return None
        na,nb=headA,headB
        if la>lb:
            i=0
            while i<la-lb:
                na=na.next
                i+=1
        else:
            i=0
            while i<lb-la:
                nb=nb.next
                i+=1
        while na!=nb:
            na=na.next
            nb=nb.next
        return na