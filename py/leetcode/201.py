class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m==0:
            return 0
        i=0
        while i<32:
            mask=(m>>i)&1
            if mask and m+(1<<i)<=n:
                m=m&(~(1<<i))
            i+=1
        return m
                

print(Solution().rangeBitwiseAnd(3,3))