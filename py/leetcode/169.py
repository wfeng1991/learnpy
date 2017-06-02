class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)//2
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        i = -1
        for k in dic:
            if dic[k]>=n:
                n=dic[k]
                i=k
        return i        
        
        