class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic=dict()
        count=0
        m=0
        dic[0]=-1
        for i,v in enumerate(nums):
            if v==0:
                count-=1
            else:
                count+=1
            if count in dic:
                m=max(m,i-dic[count])
            else:
                dic[count]=i
        return m

print(Solution().findMaxLength([0,1,1]))
