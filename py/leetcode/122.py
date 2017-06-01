class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0 
        l = len(prices)
        for i in range(0, l):
            t = i+1
            if t<l:
                if prices[i]<prices[t]:
                    m += prices[t]-prices[i]
        return m

print(Solution().maxProfit([]))
