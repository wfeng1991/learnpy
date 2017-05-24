class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = 0
        j = 0
        while j<l:
            while i<l and nums[i] != 0:
                i += 1
            j = i+1
            while j<l and nums[j] == 0:
                j += 1
            if j<l:
                t = nums[i]
                nums[i]=nums[j]
                nums[j]=t

            



        