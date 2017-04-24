class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 2:
            return min(height[0], height[1])*1
        left = 0
        right = len(height)-1
        maxA = 0
        while(left < right):
            maxA = max(maxA, min(height[left], height[right])*(right-left))
            if height[left] < height[right]:
                left = left+1
            else:
                right = right-1
        return maxA

    
s = Solution()
s = s.maxArea([2,3,4,5,18,17,6])
print(s)
                