class Solution(object):
    def findMaxForm1(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int 0
        :type n: int 1
        :rtype: int
        """
        self.cnt=0
        self.res=0
        def help(strs,i,m,n):
            self.res=max(self.res,self.cnt)
            if i<len(strs):
                m0=strs[i].count('0')
                n1=strs[i].count('1')
                if m0<=m and n1<=n:
                    self.cnt+=1
                    help(strs,i+1,m-m0,n-n1)
                    self.cnt-=1
                    help(strs,i+1,m,n)
                else:
                    help(strs,i+1,m,n)
        help(strs,0,m,n)
        return self.res

    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int 0
        :type n: int 1
        :rtype: int
        """
        dp=[[0]*(n+1) for _ in range(m+1)]
        for s in strs:
            m0=s.count('0')
            n1=s.count('1')
            i=m
            while i>=m0:
                j=n
                while j>=n1:
                    dp[i][j]=max(dp[i][j],dp[i-m0][j-n1]+1)
                    j-=1
                i-=1
        return dp[m][n]

print(Solution().findMaxForm( ["10", "1", "0"], 1, 1))