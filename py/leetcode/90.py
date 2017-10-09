class Solution(object):
    def subsetsWithDup1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        def help(nums,t,res):
            if len(nums)==0 and sorted(t) not in res:
                res.append(t)
            for i,n in enumerate(nums):
                help(nums[i+1:],t+[n],res)
                help(nums[i+1:],t,res)
        help(nums,[],res)
        return res

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[[]]
        def help(nums,t,res):
            pre=None
            for i,n in enumerate(nums):
                if pre!=n:
                    res.append(t+[n])
                    help(nums[i+1:],t+[n],res)
                pre=n
        help(sorted(nums),[],res)
        return res

print(Solution().subsetsWithDup([4,4,4,1,4]))