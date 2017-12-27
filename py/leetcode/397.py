class Solution:
    def integerReplacement1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 0
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(3,n+1):
            if i%2:
                dp[i]=min(dp[(i+1)//2],dp[(i-1)//2])+2
            else:
                dp[i]=dp[i//2]+1 
        return dp[n]
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        def help(n,mem):
            if n in mem:
                return mem[n]
            if n==1:
                mem[n] = 0
            if n%2==0:
                mem[n] = help(n//2,mem)+1
            else:
                mem[n] = min(help(n+1,mem),help(n-1,mem))+1
            return mem[n]
        return help(n,{})



print(Solution().integerReplacement(100000))
