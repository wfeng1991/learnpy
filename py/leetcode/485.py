class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        t = 0
        last = True
        for i in nums:
            if i==1 and (t==0 or last):
                t += 1
                last = True
                max = t if t>max else max
            else:
                last = False
                t = 0
        return max
