class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def isApla(c):
            n = ord(c)
            if 122>=n>=97 or 90>=n>=65 or 57>=n>=48:
                return True
            return False
        l=len(s)-1
        i,j=0,l
        while i<=l and j>=0:
            a=s[i]
            while i<=l and not isApla(s[i]):
                i+=1
                a=s[i] if i<=l else None
            b=s[j]
            while j>=0 and not isApla(s[j]):
                j-=1
                b=s[j] if j>=0 else None
            if a==b or abs(ord(a)-ord(b))==32 and (ord(a)>=65 and ord(b)>=65):
                i+=1
                j-=1
            else:
                return False
        return True

print(Solution().isPalindrome(" 3?8044''0''tt08?3"))
