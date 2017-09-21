class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # F(i, n) = G(i-1) * G(n-i)	1 <= i <= n 
        # G(n) = G(0) * G(n-1) + G(1) * G(n-2) + … + G(n-1) * G(0) 
        G=[0]*(n+1)
        G[0]=G[1]=1
        i=2
        while i<n+1:
            j=1
            while j<=i:
                G[i]+=G[j-1]*G[i-j]
                j+=1
            i+=1
        return G[n]