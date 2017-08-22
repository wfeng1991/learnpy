class Solution(object):
    def findTargetSumWays1(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        self.cnt=0
        def help(nums,i,t,s):
            if t==s and i==len(nums):
                self.cnt+=1
            if i<len(nums):
                help(nums,i+1,-1*nums[i]+t,s)
                help(nums,i+1,nums[i]+t,s)
        help(nums,0,0,S)
        return self.cnt

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        if S>1000:
            return 0
        l=len(nums)
        dp=[[0]*2001 for _ in range(l)]
        dp[0][nums[0]+1000]+=1
        dp[0][-nums[0]+1000]+=1
        for i,n in enumerate(nums):
            if i==0:
                continue
            for j in range(-1000,1000):
                if dp[i-1][j+1000]>0:
                    dp[i][j-n+1000]+=dp[i-1][j+1000]
                    dp[i][j+n+1000]+=dp[i-1][j+1000]
        return dp[l-1][S+1000]

print(Solution().findTargetSumWays([1, 1, 1, 1, 1, 1],4))