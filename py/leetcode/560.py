class Solution(object):
    def subarraySum1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l=len(nums)
        i=0
        r=0
        while i<l:
            j=i
            subsum=0
            while j<l:
                subsum+=nums[j]
                if subsum==k:
                    r+=1
                j+=1
            i+=1
        return r
    
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        dic = dict()
        subsum=0
        r=0
        for i in nums:
            if subsum in dic:
                dic[subsum]+=1
            else:
                dic[subsum]=1
            subsum+=i
            if subsum-k in dic:
                r+=dic[subsum-k]
        return r