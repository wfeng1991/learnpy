class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l=len(citations)
        if l==0:
            return 0
        t=[0]*(l+1)
        for c in citations:
            if c>l:
                t[-1]+=1
            else:
                t[c]+=1
        p=0
        i=l
        while i>=0:
            p+=t[i]
            if p>=i:
                return i
            i-=1
        return 0
        

print(Solution().hIndex([1]))