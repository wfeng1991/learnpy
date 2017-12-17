class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        start,end=-1,-1
        l = len(nums)
        low,high=0,l-1
        while low<=high:
            mid=(low+high)>>1
            if nums[mid]==target:
                start,end=mid,mid
                while start>0 and nums[start-1]==target:
                    start-=1
                while end+1<l and nums[end+1]==target:
                    end+=1
                return [start,end]
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return [start,end]
