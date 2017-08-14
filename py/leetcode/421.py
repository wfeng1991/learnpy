class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask=0
        m=0
        for i in range(0,32)[::-1]:
            mask |= 1<<i
            s=set([x&mask for x in nums])
            t=m|(1<<i)
            for p in s:
                if (p^t) in s:
                    m=t
        return m

print(Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]))
        
        