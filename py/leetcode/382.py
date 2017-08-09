# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head=head
        self.listlen=-1
        self.dic=dict()

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        import random
        if self.listlen==-1:
            self.__listlen(self.head)
        l = random.randint(1, self.listlen)
        return self.dic[l]

        
        
    def __listlen(self,head):
        t=head
        i=1
        self.listlen=0
        while t:
            self.dic[i]=t.val
            i+=1
            self.listlen+=1
            t=t.next


        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()