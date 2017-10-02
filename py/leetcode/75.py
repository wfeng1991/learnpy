class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        i=j=0
        p=l-1
        while j<=p and i<=p:
            if nums[j]==0:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j+=1
            elif nums[j]==1:
                j+=1
            else:
                nums[j],nums[p]=nums[p],nums[j]
                p-=1
Solution().sortColors([2,0,1,1,0])