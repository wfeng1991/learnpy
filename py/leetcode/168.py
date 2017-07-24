class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r=''
        while n>0:
            c=(n-1)%26
            r=chr(c+65)+r
            n=(n-1)//26
        return r

print(Solution().convertToTitle(52))
