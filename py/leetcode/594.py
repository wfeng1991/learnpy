class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        v = sorted(dic.keys())
        if len(v)<2:
            return 0
        else:
            m = 0
            for n in range(1, len(v)):
                if v[n]-v[n-1]==1:
                    m = max(m, dic[v[n-1]]+dic[v[n]])
            return m

    
print(Solution().findLHS([1,3,5,6,9,11,13,15,17]))

        