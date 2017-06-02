# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        pre = None
        r = cur
        while cur:
            t = cur.next
            cur.next=pre
            r = cur
            pre=cur
            cur=t
        return r

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

    


n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n = Solution().reverseList(n)
while n:
    print(n.val)
    n=n.next