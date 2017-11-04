class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic={}#[start,end,freq]
        m=0
        for i,n in enumerate(nums):
            if n in dic:
                dic[n][1]=i
                dic[n][2]+=1
            else:
                dic[n]=[i,i,1]
            if dic[n][2]>m:
                m=dic[n][2]
        l=len(nums)
        for i in dic:
            if dic[i][2]==m:
                l=min(l,dic[i][1]-dic[i][0]+1)
        return l