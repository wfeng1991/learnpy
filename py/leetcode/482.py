class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        l=len(S)
        i=l-1
        r=''
        p=0
        while i>=0:
            if S[i]=='-':
                i-=1
                continue
            if p<K:
                p+=1
                r=S[i].upper()+r
            else:
                r=S[i].upper()+'-'+r
                p=1
            i-=1
        return r

print(Solution().licenseKeyFormatting("---",3))