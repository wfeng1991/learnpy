class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        def prime(n):
            if n<=3:
                return 0
            for i in range(n-1,1,-1):
                if n%i==0:
                    return n//i
        if n==1:
            return 0
        else:
            cnt=0
            while prime(n):
                t=prime(n)
                n=n//t
                cnt+=t
            if n!=1:
                cnt+=n
            return cnt
       

print(Solution().minSteps(12))