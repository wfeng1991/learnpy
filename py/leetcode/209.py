class Solution:
    def minSubArrayLen1(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        l=len(nums)
        sz=l
        for i in range(l):
            j=i
            sm=0
            while j<l:
                sm+=nums[j]
                j+=1
                if sm>=s:
                    sz=min(j-i,sz)
                    if sz==1:
                        return sz
                    break
        return sz

    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums) < s:
            return 0
        start,end=0,0
        l=len(nums)
        size=l
        t=0
        while start<l:
            while t<s and end<l:
                t+=nums[end]
                end+=1
            if t>=s:
                size=min(size,end-start)
            t-=nums[start]
            start+=1
        return size
            
            

print(Solution().minSubArrayLen(7,[2,2,3,1,3,4]))   
        

