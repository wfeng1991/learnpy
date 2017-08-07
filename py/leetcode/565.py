class UnionFind:
    def __init__(self, n):
        self.cnt=[1 for i in range(0,n)]
        self.uf=[i for i in range(0,n)]
    
    def union(self,i,j):
        ir = self.findroot(i)
        jr = self.findroot(j)
        if ir!=jr:
            self.uf[jr]=ir
            self.cnt[ir]+=self.cnt[jr]
    
    def findroot(self, i):
        while self.uf[i]!=i:
            i=self.uf[i]
        return i
    
    def ufcnt(self):
        return self.cnt

class Solution:
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        unionFind = UnionFind(l)
        for i,v in enumerate(nums):
            unionFind.union(i,v)
        cnt = unionFind.ufcnt()
        return max(cnt)

print(Solution().arrayNesting([5,4,0,3,1,6,2]))




            