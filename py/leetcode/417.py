class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0:
            return []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(matrix, visited, directions, i, j, high):
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] < high:
                return
            if visited[i][j]:
                return
            visited[i][j] = True
            for (p, q) in directions:
                dfs(matrix, visited, directions, i + p, j + q, matrix[i][j])
        pacific = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        atlantic = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix[0])):
            dfs(matrix, pacific, directions, 0, i, 0)
            dfs(matrix, atlantic, directions, len(matrix)-1, i, 0)
        for i in range(len(matrix)):
            dfs(matrix, pacific, directions, i, 0, 0)
            dfs(matrix, atlantic, directions, i, len(matrix[0])-1, 0)
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if pacific[i][j] and atlantic[i][j]:
                    res.append([i, j])
        return res
print(Solution().pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))