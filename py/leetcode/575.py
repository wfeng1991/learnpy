class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        half = len(candies)//2
        s = set(candies)
        sl = len(s)
        if sl>=half:
            return half
        else:
            return sl
print(Solution().distributeCandies([1,1,1,1,2,2,2,3,3,3]))   