class Solution(object):
    def countPrimes1(self, n):
        """
        :type n: int
        :rtype: int
        """
        r=[x for x in range(2,n)]
        for i in r:
            r=[x for x in r if x%i!=0 or x==i] 
        return len(r)

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        r=[2]
        for x in range(3,n):
            isprime=True
            for j in r:
                if x%j==0:
                    isprime=False
                    break
            if isprime:
                r.append(x)
        return len(r)
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isprime=[True]*n
        for x,f in enumerate(isprime):
            if x>=2 and f:
                isprime[x * x: n: x] = [False] * len(isprime[x * x: n: x])
        return sum(isprime)



print(Solution().countPrimes(1500000))