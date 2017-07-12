class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        r = 0
        t = n//5
        while t!=0:
            r+=t
            t//=5
        return r
