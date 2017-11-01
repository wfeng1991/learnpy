class Solution(object):
    def updateMatrix1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return matrix
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    continue
                else:
                    matrix[i][j]=float('inf')
                    for k in range(len(matrix)):
                        for c in range(len(matrix[0])):
                            if matrix[k][c]==0:
                                matrix[i][j]=min(matrix[i][j],abs(i-k)+abs(j-c))
        return matrix

    def updateMatrix2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return matrix
        z=[]
        res=[[float('inf')]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    z.append([i,j])
                    res[i][j]=0
        dr=[[1,0],[-1,0],[0,1],[0,-1]]
        while z:
            (i,j)=z.pop()
            for (x,y) in dr:
                if 0<=i+x<len(matrix) and 0<=j+y<len(matrix[0]) and res[i+x][j+y]>res[i][j]+1:
                    res[i+x][j+y]=res[i][j]+1
                    z.append([i+x,j+y])
        return res
        
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix)==0 or len(matrix[0])==0:
            return matrix
        res=[[float('inf')]*len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    res[i][j]=0
                else:
                    if i>0:
                        res[i][j]=min(res[i][j],res[i-1][j]+1)
                    if j>0:
                        res[i][j]=min(res[i][j],res[i][j-1]+1)
        for i in range(len(matrix)-1,-1,-1):
            for j in range(len(matrix[0])-1,-1,-1):
                if i+1<len(matrix):
                    res[i][j]=min(res[i][j],res[i+1][j]+1)
                if j+1<len(matrix[0]):
                    res[i][j]=min(res[i][j],res[i][j+1]+1)
        return res
        

print(Solution().updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
