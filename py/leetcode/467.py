class Solution(object):
    def findSubstringInWraproundString(self, p):
        """
        :type p: str
        :rtype: int
        """
        cnt=[0]*26
        maxlen=0
        for i,c in enumerate(p):
            if i>0 and (ord(c)-ord(p[i-1])==1 or ord(p[i-1])-ord(c)==25):
                maxlen+=1
            else:
                maxlen=1
            cnt[ord(c)-ord('a')]=max(maxlen,cnt[ord(c)-ord('a')])
        return sum(cnt)

        
        
    def kmp(self,s,p):
        if len(s)<len(p):
            return -1
        nexts=[-1]*len(p)
        i,j=0,1
        while j<len(p):
            if p[i]==p[j]:
                nexts[j]=i
            else:
                t=nexts[j-1]
                while t>-1 and p[j]!=p[t]:
                    t=nexts[t]
                nexts[j]=nexts[t]+1
            i=nexts[j]
            j+=1
        i,j=0,0
        while i<len(s):
            while i<len(s) and j<len(p) and s[i]==p[j]:
                i+=1
                j+=1
            if j==len(p):
                return i-j
            j=nexts[j]
            i+=1
            j+=1
        return -1
print(Solution().findSubstringInWraproundString('zab'))
            


                
