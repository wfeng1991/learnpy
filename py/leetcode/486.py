class Solution(object):
    def PredictTheWinner1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def winner(nums,s,e,turn):
            if s==e:
                return turn*nums[s]
            a=turn*nums[s]+winner(nums,s+1,e,-turn)
            b=turn*nums[e]+winner(nums,s,e-1,-turn)
            return turn*max(turn*a,turn*b)
        return winner(nums,0,len(nums)-1,1)>=0

    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        dp=[[0 for i in nums] for i in nums]
        for i,v in enumerate(nums):
            dp[i][i]=v
        i=n-2
        while i>=0:
            j=i+1
            while j<n:
                dp[i][j]=max(nums[i]-dp[i+1][j],nums[j]-dp[i][j-1])
                j+=1
            i-=1
        return dp[0][n-1]>=0


print(Solution().PredictTheWinner([1,5,2]))     
