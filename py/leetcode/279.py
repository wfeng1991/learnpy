class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        from math import sqrt 
        cnt=[float('inf')]*(n+1)
        cnt[0]=0
        cnt[1]=1
        for i in range(2,n+1):
            j=1
            while i>=j*j:
                cnt[i]=min(cnt[i],cnt[i-j*j]+1)
                j+=1
        return cnt[-1]

print(Solution().numSquares(12))