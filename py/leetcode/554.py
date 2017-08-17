class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        n=len(wall)
        if n==0:
            return 0
        m=sum(wall[0])
        dic={}
        r=0
        for i,w in enumerate(wall):
            t=0
            for j,v in enumerate(w):
                t+=v
                if t in dic:
                    dic[t]+=1
                    if t<m:
                        r=max(dic[t],r)
                else:
                    dic[t]=1
                    if t<m:
                        r=max(1,r)
        return n-r
print(Solution().leastBricks([[100000000],[100000000],[100000000]]))