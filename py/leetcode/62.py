class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        m=m-1
        n=n-1
        t=m+n
        r=1
        i=0
        while i<n:
            r*=t
            i+=1
            t-=1
        p=1
        for i in range(1,n+1):
            p*=i
        return r//p

print(Solution().uniquePaths(4,3))
