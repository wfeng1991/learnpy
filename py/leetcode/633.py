class Solution(object):
    def judgeSquareSum1(self, c):
        """
        :type c: int
        :rtype: bool
        """
        def binarySearch(s, e, t):
            if s>e:
                return False
            mid = (s+e)//2
            if mid*mid==t:
                return True
            elif mid*mid>t:
                return binarySearch(s,mid-1,t)
            else:
                return binarySearch(mid+1,e,t)
        a = 0
        while a*a<=c:
            b=c-a*a
            f = binarySearch(0,b,b)
            if f:
                return True
            else:
                a+=1
        return False
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        a = 2
        while a*a<=c:
            count = 0
            if c % a == 0:
                while c % a == 0:
                    count+=1
                    c /= a
                if a % 4 == 3 and count % 2 != 0:
                    return False
            a+=1
        return c % 4 != 3

print(Solution().judgeSquareSum(2147483645))
            