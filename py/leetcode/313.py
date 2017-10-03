class Solution(object):
    def nthSuperUglyNumber1(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res=[1]
        p=1
        while p<n:
            t=[i*j for i in primes for j in res if i*j>res[-1]]
            res.append(min(t))
            p+=1
        return res[-1]

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        res=[1]
        idx=[0]*len(primes)
        p=1
        while p<n:
            res.append(min([res[idx[i]]*primes[i] for i in range(len(primes))]))
            j=0
            while j<len(primes):
                while res[idx[j]]*primes[j]<=res[-1]:
                    idx[j]+=1
                j+=1
            p+=1
        return res[-1]


print(Solution().nthSuperUglyNumber(12,[2, 7, 13, 19]))
