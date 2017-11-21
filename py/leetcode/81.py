class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        h=len(nums)-1
        l=0
        while l<=h:
            if nums[l]==target or nums[h]==target:
                return True
            mid=(l+h)>>1
            if nums[mid]==target:
                return True
            if nums[mid]>nums[h]:
                if nums[mid]>target>=nums[l]:
                    h=mid-1
                else:
                    l=mid+1
            elif nums[mid]<nums[h]:
                if nums[mid]<target<=nums[h]:
                    l=mid+1
                else:
                    h=mid-1
            else:
                h-=1
        return False
            
print(Solution().search([15,16,19,20,25,1,3,4,5,7,10,14],25))

        