class Solution(object):
    '''
    Below is my explanation of the following neat solution 
    where we sort people from tall to short (and by increasing k-value) 
    and then just insert them into the queue using their k-value as the queue index
    '''
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda h, k:(-h, k))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue