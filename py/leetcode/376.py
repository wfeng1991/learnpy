class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l==0:
            return 0
        cnt,i=1,1
        bigger=None
        while i<l:
            if nums[i]!=nums[i-1]:
                t=nums[i]>nums[i-1]
                if bigger != t:
                    bigger=t
                    cnt+=1
            i+=1
        return cnt

print(Solution().wiggleMaxLength([1,1]))
                
            
