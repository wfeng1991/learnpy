class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        ml=0
        r=''
        for t in d:
            if len(t)>=ml:
                i=j=0
                while i<len(s) and j<len(t):
                    if s[i]==t[j]:
                        i+=1
                        j+=1
                    else:
                        i+=1
                if j==len(t):
                    ml=max(ml,j)
                    if not r:
                        r=t
                    elif len(r)<j:
                        r=t
                    elif len(r)==j and r>t:
                        r=t
        return r

print(Solution().findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
