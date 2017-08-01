class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        l = len(nums)
        if l==1:
            return str(nums[0])
        if l==2:
            return str(nums[0])+'/'+str(nums[1])
        r=str(nums[0])
        i=1
        while i<l:
            if i==1:
                r+='/('+str(nums[i])
            else:
                r+='/'+str(nums[i])
            i+=1
        r+=')'
        return r