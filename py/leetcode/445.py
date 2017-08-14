# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def res(node):
            if not node or not node.next:
                return node
            if node and node.next:
                head = res(node.next)
                node.next.next=node
                node.next=None
            return head
        l1=res(l1)
        l2=res(l2)
        head=ListNode(0)
        t=head
        carry=0
        while l1 or l2:
            if l1 and l2:
                s=l1.val+l2.val+carry
                carry=s//10
                t.next=ListNode(s%10)
            elif l1:
                s=l1.val+carry
                carry=s//10
                t.next=ListNode(s%10)
            elif l2:
                s=l2.val+carry
                carry=s//10
                t.next=ListNode(s%10)
            t=t.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        if carry:
            t.next=ListNode(carry)
        return res(head.next)

l1=ListNode(1)
l1.next=ListNode(2)
l2=ListNode(1)
l2.next=ListNode(9)

t=Solution().addTwoNumbers(l1,l2)
