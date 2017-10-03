class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p=[-float('inf')]+nums+[-float('inf')]
        l=len(p)
        i=1
        while i<l-1:
            if p[i-1]<p[i] and p[i]>p[i+1]:
                return i-1
            i+=1
        