class Solution(object):
    def searchMatrix1(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        if n==0:
            return False
        i=0
        while i<m:
            arr=matrix[i]
            if arr[0]<=target and arr[-1]>=target:
                j=0
                while j<=n:
                    mid=(j+n)//2
                    if arr[mid]>target:
                        n=mid-1
                    elif arr[mid]<target:
                        j=mid+1
                    else:
                        return True
            i+=1
        return False

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=len(matrix)
        if m==0:
            return False
        n=len(matrix[0])
        if n==0:
            return False
        row=0
        col=n-1
        while row<m and col>=0:
            if matrix[row][col]>target:
                col-=1
            elif matrix[row][col]<target:
                row+=1
            else:
                return True
        return False


print(Solution().searchMatrix([
[1,2,3,4,5],
[6,7,8,9,10],
[11,12,13,14,15],
[16,17,18,19,20],
[21,22,23,24,25]],14))
        
