class Solution:
    def findMinHeightTrees1(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        import collections
        graph=collections.defaultdict(list)
        for (p,q) in edges:
            graph[p]+=q,
            graph[q]+=p,
        self.h=-1
        self.res=[]
        def bfs(graph,n,h):
            g=[]
            gh=graph[n]
            seen=set([n])
            while gh:
                h+=1
                for p in gh:
                    seen.add(p)
                    for j in graph[p]:
                        if j not in seen:
                            g.append(j)
                            seen.add(j)
                gh=g
                g=[]
            if self.h==-1:
                self.h=h
                self.res=[n]
            elif self.h>h:
                self.h=h
                self.res=[n]
            elif self.h==h:
                self.res+=n,
        for i in range(n):
            bfs(graph,i,0)
        return self.res

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n<3:
            return [i for i in range(n)]
        import collections
        graph=collections.defaultdict(list)
        degree=[0]*n
        for (p,q) in edges:
            graph[p]+=q,
            graph[q]+=p,
            degree[p]+=1
            degree[q]+=1
        leaf=[i for i,l in enumerate(degree) if l==1]
        while n>2:
            n-=len(leaf)
            new_leaf=[]
            for i in leaf:
                p=graph[i].pop()
                graph[p].remove(i)
                if len(graph[p])==1:
                    new_leaf+=p,
            leaf=new_leaf
        return leaf

        
        

print(Solution().findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))

        
                

            

