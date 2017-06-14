class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            dic[n]=True
        for n in range(0, len(nums)+1):
            if n not in dic:
                return n

print(Solution().missingNumber([0,3,4,2]))
        