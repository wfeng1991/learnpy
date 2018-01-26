class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s)<4 or len(s)>12:
            return []
        def isvaild(s):
            if s and str(int(s))==s and int(s)<=255:
                return True
            return False
        res=[]
        i=1
        while i<4:
            j=i+1
            while j<i+4:
                k=j+1
                while k<j+4:
                    s1,s2,s3,s4=s[:i],s[i:j],s[j:k],s[k:]
                    if isvaild(s1) and isvaild(s2) and isvaild(s3) and isvaild(s4): 
                        res.append(s1+'.'+s2+'.'+s3+'.'+s4)
                    k+=1
                j+=1
            i+=1
        return res
print(Solution().restoreIpAddresses("010010"))

