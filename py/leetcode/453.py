# let's define sum as the sum of all the numbers, before any moves; minNum as the min number int the list; n is the length of the list;

# After, say m moves, we get all the numbers as x , and we will get the following equation

#  sum + m * (n - 1) = x * n
# and actually,

#   x = minNum + m
# and finally, we will get

#   sum - minNum * n = m
# So, it is clear and easy now.

class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = min(nums)
        n = len(nums)
        return sum(nums)-m*n

print(Solution().minMoves([1,2,3424]))# [5,6,8,8,5]
        

