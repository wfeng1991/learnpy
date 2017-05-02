# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(None)
        t = head
        c = None
        while len(lists) != 0:
            for node in lists:
                if c is None or (node is not None and c.val > node.val):
                    c = node
            lists.remove(c)
            if c is not None:
                t.next = c
                t = t.next
                c = c.next
                if c is not None:
                    lists.append(c)
                c = None
        return head.next
            