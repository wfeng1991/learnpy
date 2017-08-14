class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction=[[-1,1],[1,-1]]
        col=len(matrix)
        if col==0:
            return []
        row=len(matrix[0])
        r=[]
        i,j=0,0
        cnt=0
        while True:
            r.append(matrix[i][j])
            if i==col-1 and j==row-1:
                break
            i+=direction[cnt%2][0]
            j+=direction[cnt%2][1]
            if i==col:
                i=col-1
                j+=2
                cnt+=1
            elif j==row:
                j=row-1
                i+=2
                cnt+=1
            elif i<0:
                i=0
                cnt+=1
            elif j<0:
                j=0
                cnt+=1
        return r

print(Solution().findDiagonalOrder([[ 1, 2, 3 ], [ 4, 5, 6 ], [ 7, 8, 9 ]]))