class Solution(object):
    def minimumTotal1(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        self.res=float('inf')
        def help(triangle,level,index,t):
            if level==len(triangle):
                self.res=min(self.res,t)
            if level<len(triangle):
                if index+1<len(triangle[level]):
                    help(triangle,level+1,index,t+triangle[level][index])
                    help(triangle,level+1,index+1,t+triangle[level][index+1])
                else:
                    help(triangle,level+1,index,t+triangle[level][index])
        help(triangle,0,0,0)
        return self.res

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        level=len(triangle)-1
        dp=[x for x in triangle[-1]]
        for i in range(level,0,-1):
            paths=len(triangle[i])-1
            for j in range(paths):
                dp[j]=min(dp[j],dp[j+1])+triangle[i-1][j]
        return dp[0]


print(Solution().minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))