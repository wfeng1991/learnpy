class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.r=[]
        def help(nums,res):
            if not nums:
                self.r.append(res)
            for i,n in enumerate(nums):
                help(nums[:i]+nums[i+1:],res+[n])
        help(nums,[])
        return self.r

print(Solution().permute([1,2,3]))