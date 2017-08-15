class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        times=sorted(timePoints,key=lambda t:(t.split(':')[0],t.split(':')[1]))
        l=len(times)
        i=0
        m=float('inf')
        while i<l-1:
            hm=times[i].split(':')
            t1=int(hm[0])*60+int(hm[1])
            hm1=times[i+1].split(':')
            t2=int(hm1[0])*60+int(hm1[1])
            m=min(m,t2-t1)
            i+=1
        hm=times[0].split(':')
        t1=int(hm[0])*60+int(hm[1])+24*60
        hm1=times[-1].split(':')
        t2=int(hm1[0])*60+int(hm1[1])
        m=min(m,t1-t2)
        return m


print(Solution().findMinDifference(["23:59","00:00","22:12","22:10"]))