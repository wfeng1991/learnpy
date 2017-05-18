class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count = 0
        rows = len(grid)
        if rows == 0:
            return count
        cols = len(grid[0])
        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == 1:
                    up = 0
                    down = 0
                    left = 0
                    right = 0
                    if i+1 < rows:
                        down = grid[i + 1][j]
                    if i-1 >= 0:
                        up = grid[i - 1][j]
                    if j-1 >= 0:
                        left = grid[i][j - 1]
                    if j+1 < cols:
                        right = grid[i][j + 1]
                    count += 4 - (up+down+left+right)
        return count
