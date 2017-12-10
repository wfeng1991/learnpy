class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        high=len(nums)-1
        low=0
        while low<=high:
            mid=(low+high)>>1
            t=nums[mid]
            if t==target:
                return mid
            elif nums[low]<t:
                if nums[low]<=target<t:
                    high=mid-1
                else:
                    low=mid+1
            elif nums[low]>t:
                if t<target<=nums[high]:
                    low=mid+1
                else:
                    high=mid-1
            else:
                low+=1
        return -1

print(Solution().search([1,3,5],1))