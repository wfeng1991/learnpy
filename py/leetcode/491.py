class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=len(nums)
        if l<2:
            return []
        def help(nums,t,res):
            if len(t)>1:
                res.append(t)
            used=set()
            for i,v in enumerate(nums):
                if v in used:
                    continue
                if len(t)==0 or t[-1]<=v:
                    used.add(v)
                    help(nums[i+1:],t+[v],res)
        res=[]
        help(nums,[],res)
        return res

print(Solution().findSubsequences([4,6,7,7]))