class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ptn = ''
        l = len(s)
        if l<2:
            return False

        i = 0
        while i<l/2:
            ptn+=s[i]
            lp=i+1
            j=lp
            while j<l:
                if s[j]==ptn[j%lp]:
                    j+=1
                    if j==l and l%lp==0:
                        return True
                else:
                    break
            i+=1
        return False

print(Solution().repeatedSubstringPattern('aaa'))