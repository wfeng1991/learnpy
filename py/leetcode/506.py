class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        t = [x for x in nums]
        t.sort(reverse=True)
        dic = {}
        i=0
        while i < len(t):
            if i==0:
                dic[t[i]]="Gold Medal"
            elif i==1:
                dic[t[i]]="Silver Medal"
            elif i==2:
                dic[t[i]]="Bronze Medal"
            else:
                dic[t[i]]=str(i+1)
            i+=1
        return [dic[i] for i in nums]

print(Solution().findRelativeRanks([1,2,8,4,5]))