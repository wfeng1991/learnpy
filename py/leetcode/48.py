class Solution(object):
    def rotate1(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # not in-place
        length=len(matrix)
        if length==0:
            return []
        res=[]
        t=[]
        cur=matrix[0]
        for i in range(length):
            for l in matrix:
                t=[l[i]]+t
            res.append(t)
            t=[]
        matrix = res

    def rotate2(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l=len(matrix)
        clcles=l//2
        pp=l-1
        for i in range(clcles):
            t=pp-i*2
            for j in range(t):
                p=matrix[i][i]
                for k in range(i+1,l-i):
                    matrix[k-1][i]=matrix[k][i]
                for k in range(i+1,l-i):
                    matrix[l-1-i][k-1]=matrix[l-1-i][k]
                for k in range(l-i-1,i,-1):
                    matrix[k][l-1-i]=matrix[k-1][l-1-i]
                for k in range(l-i-1,i,-1):
                    matrix[i][k]=matrix[i][k-1]
                matrix[i][i+1]=p

    # best
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # \ flip
        for i in xrange(n):
            for j in xrange(i,n):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
                
        # | flip
        for i in xrange(n):
            for j in xrange(n/2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[i][n-1-j]
                matrix[i][n-1-j] = tmp

print(Solution().rotate([[2,29,20,26,16,28],[12,27,9,25,13,21],[32,33,32,2,28,14],[13,14,32,27,22,26],[33,1,20,7,21,7],[4,24,1,6,32,34]]))


       

