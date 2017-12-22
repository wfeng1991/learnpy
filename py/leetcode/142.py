# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #暴力解法 先判断是否有环 然后找到第一个在环中的node
        has_cycle=False
        one_step=head
        two_step=head
        while two_step and two_step.next:
            one_step=one_step.next
            two_step=two_step.next.next
            if one_step==two_step:
                has_cycle=True
                break
        if not has_cycle:
            return None
        p=head
        start=one_step.next
        while start:
            if start==p:
                return p
            if start==one_step:
                p=p.next
            start=start.next
        return None

    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #先判断是否有环(快慢指针法) 
        has_cycle=False
        one_step=head
        two_step=head
        while two_step and two_step.next:
            one_step=one_step.next
            two_step=two_step.next.next
            if one_step==two_step:
                has_cycle=True
                break
        if not has_cycle:
            return None
        p=head
        start=one_step
        while True:
            if start==p:
                return p
            start=start.next
            p=p.next
        return None
        