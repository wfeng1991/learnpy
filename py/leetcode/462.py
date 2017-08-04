class Solution(object):
    def minMoves21(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # from functools import reduce
        # sumv=reduce(lambda x,y:x+y,nums)
        m=float('inf')
        for n in nums:
            t=0
            for i in nums:
                if i!=n:
                    t+=abs(n-i)
            m=min(m,t)
        return m

    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        median = sorted(nums)[len(nums) / 2]
        return sum(abs(num - median) for num in nums)
