class Solution(object):

    def uniquePathsWithObstacles1(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        self.cnt = 0

        def help(obstacleGrid, x, y, m, n):
            if obstacleGrid[x][y]:
                return
            if obstacleGrid[x][y] == 0 and x == m - 1 and y == n - 1:
                self.cnt += 1
            if x < m and y < n:
                if y + 1 < n and obstacleGrid[x][y + 1] == 0:
                    help(obstacleGrid, x, y + 1, m, n)
                if x + 1 < m and obstacleGrid[x + 1][y] == 0:
                    help(obstacleGrid, x + 1, y, m, n)
        help(obstacleGrid, 0, 0, m, n)
        return self.cnt

    def uniquePathsWithObstacles2(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        stack = [[0, 0]]
        cnt = 0
        while stack:
            x, y = stack.pop()
            if obstacleGrid[x][y]:
                continue
            if x == m - 1 and y == n - 1:
                cnt += 1
            if x + 1 < m and obstacleGrid[x + 1][y] == 0:
                stack.append([x + 1, y])
            if y + 1 < n and obstacleGrid[x][y + 1] == 0:
                stack.append([x, y + 1])
        return cnt
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        if m == 0:
            return 0
        n = len(obstacleGrid[0])
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i,row in enumerate(obstacleGrid):
            for j,v in enumerate(row):
                if v==1:
                    dp[i][j]=0
                elif j>0 and i>0:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j]
                elif i==0 and j>0:
                    dp[i][j]=dp[i][j-1]
                elif j==0 and i>0:
                    dp[i][j]=dp[i-1][j]
        return dp[-1][-1]
