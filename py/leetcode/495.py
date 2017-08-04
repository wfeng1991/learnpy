class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        timeSeries+=[float('inf')]
        l=len(timeSeries)
        i=0
        r=0
        while i+1<l:
            if timeSeries[i]+duration>timeSeries[i+1]:
                r+=timeSeries[i+1]-timeSeries[i]
            else:
                r+=duration
            i+=1
        return r

print(Solution().findPoisonedDuration([1,2,5,6], 2))