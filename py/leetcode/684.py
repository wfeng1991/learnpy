class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        class UnionFind(object):
            def __init__(self,size):
                self.data=[x for x in range(size+1)]
            
            def find(self,x):
                while self.data[x]!=x:
                    x=self.data[x]
                return x
        
            def union(self,x,y):
                tx=self.find(x)
                ty=self.find(y)
                if tx==ty:
                    return False
                self.data[tx]=ty
                return True
        size=len(edges)
        un=UnionFind(size)
        for e in edges:
            if not un.union(*e):
                return e