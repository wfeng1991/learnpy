# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head:
            p1=head.next
            p2=None
            if head.next:
                p2=head.next.next
            else:
                return False
            while p1 and p2:
                if p1==p2:
                    return True
                p1=p1.next
                if p2.next:
                    p2=p2.next.next
                else:
                    return False
            return False
        else:
            return False
