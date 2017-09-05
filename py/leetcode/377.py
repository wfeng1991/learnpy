class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        mem = dict()
        def help(nums, target, mem):
            cnt=0
            if target==0:
                return 1
            for n in nums:
                if n>target:
                    continue
                if (target-n) in mem:
                    cnt+=mem[target-n]
                else:
                    cnt+=help(nums,target-n,mem)
            mem[target]=cnt
            return cnt
        return help(nums, target, mem)
        
            
print(Solution().combinationSum4([1, 2], 10))