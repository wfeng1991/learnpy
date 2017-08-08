class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        if len(pairs)==1:
            return 1
        sp=sorted(pairs,key=lambda x:x[1])
        m=1
        pre=sp[0]
        i=1
        while i<len(sp):
            if sp[i][0]>pre[1]:
                m+=1
                pre=sp[i]
            i+=1
        return m

print(Solution().findLongestChain([[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]]))
                        