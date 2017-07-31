class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        i=0
        r=[]
        while i<l:
            t=nums[i]
            while t!=-1 and nums[t-1]!=-1:
                nums[i],nums[t-1]=nums[t-1],nums[i]
                nums[t-1]=-1
                t=nums[i]
            i+=1
        for x in nums:
            if x!=-1:
                r.append(x)
        return r

print(Solution().findDuplicates([13,8,5,3,20,12,3,20,5,16,9,19,12,11,13,19,11,1,10,2]))
