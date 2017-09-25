class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l==1:
            return nums[0]
        s=0
        e=l-1
        while s<e:
            mid=(s+e)//2
            if nums[e]>=nums[mid]>=nums[s]:
                return nums[s]
            elif nums[mid]<nums[s]:
                e=mid
                s=s+1
            elif nums[mid]>nums[e]:
                s=mid+1
        return nums[s]

print(Solution().findMin([1,2,3,1,0,1]))