class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        r=[]
        for i,row in enumerate(matrix):
            for j,v in enumerate(row):
                if v==0:
                    r.append([i,j])
        for i,j in r:
            for k,v in enumerate(matrix[i]):
                matrix[i][k]=0
            for row in matrix:
                row[j]=0
        print(matrix)

Solution().setZeroes([[0,1]])