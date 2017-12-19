class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res=[]
        if not nums:
            return res
        nums.append(float('inf'))
        start,end=nums[0],nums[0]
        i=1
        while i<len(nums):
            if end+1==nums[i]:
                end+=1
            else:
                if start==end:
                    res.append(str(start))
                else:
                    res.append(str(start)+'->'+str(end))
                start,end=nums[i],nums[i]
            i+=1
        return res
print(Solution().summaryRanges([0,1,2,4,5,7]))
