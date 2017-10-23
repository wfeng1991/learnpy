class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        def help(nums,start,end):
            rob,notrob=0,0
            for i in range(start,end):
                j,k=rob,notrob
                rob=nums[i]+k
                notrob=max(j,k)
            return max(notrob,rob)
        return max(help(nums,0,len(nums)-1),help(nums,1,len(nums)))
            
