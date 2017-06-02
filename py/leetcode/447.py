class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dic = dict()
        res = 0
        for i,p in enumerate(points):
            for j,k in enumerate(points):
                if i==j:
                    continue
                distance = pow((p[0]-k[0]),2)+pow((p[1]-k[1]),2)
                if distance in dic:
                    dic[distance]+=1
                else:
                    dic[distance]=1
            for i in dic:
                res += dic[i]*(dic[i]-1)
            dic.clear()
        return res

print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))
