class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        n=len(M)
        for i in range(0,n):
            M[i][i]=i
        for i in range(0,n):
            for j in range(0,n):
                if i!=j and M[i][j]==1:
                    t=0
                    if M[i][i]<M[j][j]:
                        t=M[j][j]
                        M[j][j]=M[i][i]
                    else:
                        t=M[i][i]
                        M[i][i]=M[j][j]
                    for k in range(0,n):
                            if M[k][k]==t:
                                M[k][k]=M[i][i]
        r=set()
        for k in range(0,n):
            r.add(M[k][k])               
        return len(r)

print(Solution().findCircleNum([[1,0,0,1],[0,1,0,0],[0,0,1,0],[1,0,0,1]]))