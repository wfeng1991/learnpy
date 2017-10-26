class Solution(object):
    def permuteUnique1(self, nums):
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

    def permuteUnique(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l)+1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i<len(l) and l[i]==n: break              #handles duplication
            ans = new_ans
        return ans
print(Solution().permuteUnique([1,2,1]))
                    