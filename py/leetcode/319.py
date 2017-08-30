class Solution(object):
    def bulbSwitch1(self, n):
        """
        :type n: int
        :rtype: int
        """
        lst=[0]*n
        i=1
        while i<=n:
            j=i-1
            while j<n:
                lst[j]=0 if lst[j]==1 else 1
                j+=i
            i+=1
        return lst.count(1)

    def bulbSwitch2(self, n):
        """
        :type n: int
        :rtype: int
        """
        def divisors(i):
            cnt=0
            for j in range(1,i+1):
                if i%j==0:
                    cnt+=1
            return cnt
        r=0
        for i in range(n):
            cnt=divisors(i+1)
            if cnt%2==1:
                r+=1
        return r

    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        return int(math.sqrt(n))
        

print(Solution().bulbSwitch(5))