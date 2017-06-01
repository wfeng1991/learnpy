class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        alph = {}
        for i,c in enumerate(range(65,91)):
            alph[chr(c)]=i+1
        r = 0
        l = len(s)-1
        i = l
        while i>=0:
            r+=alph[s[i]]*pow(26,l-i)
            i-=1
        return r


print(Solution().titleToNumber('BB'))
