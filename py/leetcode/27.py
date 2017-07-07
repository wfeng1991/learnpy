class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        begin = 0
        l = len(nums)
        for n in nums:
            if n!=val:
                nums[begin]=n
                begin+=1
        return begin
        

print(Solution().removeElement([2,2,3],2))    
