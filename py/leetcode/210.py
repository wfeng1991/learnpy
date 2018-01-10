class Solution:
    def findOrder1(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        import collections
        graph=collections.defaultdict(list)
        degree=[0]*numCourses
        for (p,q) in prerequisites:
            graph[p]+=q,
            graph[q]+=p,
            degree[p]+=1
        res=[]
        seen=set()
        while len(res)<numCourses:
            has_cycle=True
            for i,d in enumerate(degree):
                if d==0 and i not in seen:
                    has_cycle=False
                    res.append(i)
                    seen.add(i)
                    for p in graph[i]:
                        degree[p]-=1
            if has_cycle:
                return []
        return res

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        
        for x, y in prerequisites:
            graph[y].append(x)
        
        for i in range(numCourses):
            for course in graph[i]:
                indegree[course] += 1
        
        res = []
        
        queue = []
        for c in range(numCourses):
            if indegree[c] == 0:
                queue.append(c)                
                                
        while queue:
            c = queue.pop(0)
            res.append(c)
            for neighbor in graph[c]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        if len(res) == numCourses:
            return res
        else:
            return []

print(Solution().findOrder(2, [[1,0]]))



        
                
        