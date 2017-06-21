class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        p = -1
        for i,n in enumerate(nums):
            if n>target:
                p = i
                break
            elif n==target:
                p = i
                break
        
        if p==-1:
            p = len(nums)
        return p

print(Solution().searchInsert([1,3,5,6],4))