class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==2:
            return 1
        i=2
        m=0
        while i<=n-1:
            if n%i==0:
               m=max(m,pow(i,n//i))
            else:
                p=n%i
                if p==1:
                    if n//i<2:
                        m=max(m,(n-i)*i)
                    else:
                        m=max(m,pow(i,n//i-1)*(i+p))
                else:
                    t=n//i
                    m=max(m,pow(i,t)*p)
            i+=1
        return m

print(Solution().integerBreak(10))

