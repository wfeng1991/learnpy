class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s or len(s)<10:
            return []
        dic={}
        start,end=0,10
        res=set()
        while end<=len(s):
            p=s[start:end]
            if p in dic:
                res.add(p)
            else:
                dic[p]=1
            start+=1
            end+=1
        return [p for p in res]

print(Solution().findRepeatedDnaSequences('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT'))
        