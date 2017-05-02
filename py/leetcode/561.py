class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        i = 0
        l = len(nums)
        sum = 0 
        while i < l:
            sum += nums[i]
            i+=2
        return sum