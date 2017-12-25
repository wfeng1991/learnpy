class Solution(object):
    def findPaths1(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        directions=[[0,1],[0,-1],[1,0],[-1,0]]
        stack=[[i,j]]
        _stack=[]
        cnt=0
        step=N
        while stack and step:
            x,y=stack.pop()
            for p,q in directions:
                _x=p+x
                _y=q+y
                if _x<0 or _x>=m or _y<0 or _y>=n:
                    cnt+=1
                else:
                    _stack.append([_x,_y])
            if not stack:
                step-=1
                stack=_stack
                _stack=[]
        return cnt

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        M=pow(10,9)+7
        dp=[[0]*n for _ in range(m)]
        dp[i][j]=1
        count=0
        for _ in range(N):
            _dp=[[0]*n for _ in range(m)]
            for x in range(m):
                for y in range(n):
                    if x==0:
                        count+=dp[x][y]%M
                    if x==m-1:
                        count+=dp[x][y]%M
                    if y==0:
                        count+=dp[x][y]%M
                    if y==n-1:
                        count+=dp[x][y]%M
                    t=0
                    if x>0:
                        t+=dp[x-1][y]%M
                    if y>0:
                        t+=dp[x][y-1]%M
                    if x+1<m:
                        t+=dp[x+1][y]%M
                    if y+1<n:
                        t+=dp[x][y+1]%M
                    _dp[x][y]=t%M
            dp=_dp
        return count%M
            
print(Solution().findPaths(1,3,3,0,1))