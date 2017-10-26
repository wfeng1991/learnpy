class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def help(nums,t,res):
            if not nums:
                res.append(t)
            for i,n in enumerate(nums):
                if i>0 and n==nums[i-1]:
                    continue
                help(nums[:i]+nums[i+1:],t+[n],res)
        res=[]
        help(sorted(nums),[],res)
        return res
print(Solution().permuteUnique([1,2,1]))
                    