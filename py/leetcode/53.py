class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l==0:
            return 0
        m = max(nums)
        if m<=0:
            return m
        m = 0
        t = 0
        for i,n in enumerate(nums):
            t += n
            if t>m:
                m = t
            if t<=0:
                t=0           
        return m
            
