class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        w=0
        t=n
        p=t
        while t>0:
            p=t
            t=t-int(9*pow(10,w-1)*w)
            w+=1
        w-=1
        m=p//w-1+int(pow(10,w-1))
        carry = 1 if t%w else 0
        m+=carry
        return int(str(m)[p%w-1])
print(Solution().findNthDigit(1000))
