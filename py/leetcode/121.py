class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=j=-1
        m = 0
        for n in prices:   
            if i==-1 or n<i:
                i=n
                j=n
            if n>i:
                j=n
                m = max(m,j-i)
        return m

print(Solution().maxProfit([2,1,2,1,0,1,2]))        