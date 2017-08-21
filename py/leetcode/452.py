class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        l=len(points)
        if l==0:
            return 0
        cnt=1
        points = sorted(points)
        print(points)
        i=1
        r=points[0]    
        while i<l:
            p=points[i]
            if p[0]<=r[1]:
                r[0]=p[0]
                if p[1]<=r[1]:
                    r[1]=p[1]
            else:
                cnt+=1
                r=p
            i+=1
        return cnt
                  




print(Solution().findMinArrowShots([[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]))
