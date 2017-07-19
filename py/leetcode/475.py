class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses=sorted(houses)
        heaters=sorted(heaters)
        lhr=len(heaters)
        lhs=len(houses)
        m=-1
        r=0
        j=0
        for i in range(0,lhs):
            while j<lhr:
                if abs(heaters[j]-houses[i])<m:
                    m=abs(heaters[j]-houses[i])
                else:
                    j-=1
                    break
                j+=1
            if j==lhr:
                j-=1
            r=max(m,r)
            m=-1
        return r

    def findRadius1(self, houses, heaters):
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0
        for x in sorted(houses):
            while x >= sum(heaters[i:i+2]) / 2.:
                i += 1
            r = max(r, abs(heaters[i] - x))
        return r

print(Solution().findRadius(list(range(1,15226))+[1522],list(range(1,15226))+[1522]))