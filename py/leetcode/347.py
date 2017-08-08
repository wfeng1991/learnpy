class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = dict()
        for n in nums:
            if n in dic:
                dic[n]+=1
            else:
                dic[n]=1
        a = sorted(dic.items(),key=lambda x: -x[1])
        r=[]
        i=0
        while i<k:
            r.append(a[i][0])
            i+=1
        return r

print(Solution().topKFrequent([1,1,1,2,2,3],2))