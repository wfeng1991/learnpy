class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m=len(matrix)
        if m==0:
            return 0
        n=len(matrix[0])
        dp=[[0]*n for _ in range(m)]
        maxlen=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]=='1':
                    top,left,topleft=0,0,0
                    if i>0:
                        top=dp[i-1][j]
                    if j>0:
                        left=dp[i][j-1]
                    if i>0 and j>0:
                        topleft=dp[i-1][j-1]
                    dp[i][j]=min(left,topleft,top)+1
                    maxlen=max(dp[i][j],maxlen)
        return maxlen*maxlen