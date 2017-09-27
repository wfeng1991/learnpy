class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1=m2=float('inf')
        for x in nums:
            if x<=m1:
                m1=x
            elif x<=m2:
                m2=x
            else:
                return True
        return False
