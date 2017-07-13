class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0:
            return 0
        p=0
        for i in range(0,len(nums)):
            if nums[p]==nums[i]:
                nums[p]=nums[i]
            else:
                p+=1
                nums[p]=nums[i]
        return p+1  