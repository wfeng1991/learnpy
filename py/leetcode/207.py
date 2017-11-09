class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        g=[[] for _ in range(numCourses)]
        for (x,y) in prerequisites:
            g[x]+=[y]
        d=[0]*numCourses
        for n in g:
            for i in n:
                d[i]+=1
        for _ in range(numCourses):
            j=0
            while j<numCourses:
                if d[j]==0:
                    break
                j+=1
            if j==numCourses:
                return False
            d[j]=-1
            for k in g[j]:
                d[k]-=1
        return True
        
        

print(Solution().canFinish(3,[[0,2],[2,1],[2,0]]))
