class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        cnt=0
        def help(grid,x,y,visited):
            if 0<=x<len(grid) and 0<=y<len(grid[0]):
                if not visited[x][y] and grid[x][y]=='1':
                    visited[x][y]=True
                    help(grid,x+1,y,visited)
                    help(grid,x-1,y,visited)
                    help(grid,x,y-1,visited)
                    help(grid,x,y+1,visited)
                    
        visited=[[False]*len(grid[0]) for _ in range(len(grid))]
        for i,r in enumerate(grid):
            for j,s in enumerate(r):
                if visited[i][j]:
                    continue
                if grid[i][j]=='1':
                    help(grid,i,j,visited)
                    cnt+=1
        return cnt

    

            