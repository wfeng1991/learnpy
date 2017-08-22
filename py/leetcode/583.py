class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        l1=len(word1)
        l2=len(word2)
        dp=[[0]*(l2+1) for i in range(l1+1)]
        for i1,c1 in enumerate(word1):
            for i2,c2 in enumerate(word2):
                if c1==c2:
                    dp[i1+1][i2+1]=dp[i1][i2]+1
                else:
                    dp[i1+1][i2+1]=max(dp[i1+1][i2],dp[i1][i2+1])
        ml=dp[l1][l2]
        return l1+l2-ml*2

        
print(Solution().minDistance("211",'32131'))