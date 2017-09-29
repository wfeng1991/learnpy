class Solution(object):
    def canPartition1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        self.f=False
        def help(nums, i, subsum, t):
            if t==subsum:
                self.f=True
                return
            if i<len(nums) and not self.f:
                help(nums,i+1,subsum+nums[i],t)
                help(nums,i+1,subsum,t)
        s=sum(nums)
        if s%2==1:
            return self.f
        else:
            help(nums,0,0,s//2)
            return self.f
    
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = len(nums)
        s = sum(nums)
        s=sum(nums)
        if s%2==1:
            return False
        else:
            dp=[[False]*(s+1) for _ in range(l+1)]
            dp[0][0]=True
            for i in range(l+1):
                dp[i][0]=True
            for i in range(1,l+1):
                for j in range(1, s+1):
                    if j>=nums[i-1]:
                        dp[i][j]= dp[i-1][j] or dp[i-1][j-nums[i-1]]
                    else:
                        dp[i][j]= dp[i-1][j]
            return dp[l][s//2]

print(Solution().canPartition([1,2,5]))