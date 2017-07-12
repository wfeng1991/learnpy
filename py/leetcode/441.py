class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt=0
        i=1
        while n>=0:
            n-=i
            i+=1
            if n>=0:
                cnt+=1
        return cnt

print(Solution().arrangeCoins(8))