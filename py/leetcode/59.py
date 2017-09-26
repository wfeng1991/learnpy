class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res=[[0]*n for _i in range(n)]
        p=1
        t=n*n
        for i in range(0,n-1):
            lst=range(i,n-i-1)
            #top
            for j in lst:
                if p>t:
                    break
                res[i][j]=p
                p+=1

            #right
            for j in lst:
                if p>t:
                    break
                res[j][n-i-1]=p
                p+=1
                
            lst1=range(n-i-1,i,-1)
            #bot
            for j in lst1:
                if p>t:
                    break
                res[n-i-1][j]=p
                p+=1
                
            #left
            for j in lst1:
                if p>t:
                    break
                res[j][i]=p
                p+=1
        if t%2==1:
            res[n//2][n//2]=t      
        return res

print(Solution().generateMatrix(1))
