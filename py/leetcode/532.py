class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<0:
            return 0
        dic = dict()
        for x in nums:
            if x in dic:
                dic[x]+=1
            else:
                dic[x]=1
        r=0
        if k==0:
            for x in nums:
                if dic[x]>1 and dic[x]>0:
                    r+=1
                    dic[x]=0
        else:
            for x in set(nums):
                if x-k in dic and dic[x-k]>0:
                    r+=1
                    dic[x]=0
                if x+k in dic and dic[x+k]>0:
                    r+=1
                    dic[x]=0
        return r