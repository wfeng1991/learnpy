class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res=[]
        def help(candidates, target, r):
            if target<0:
                return
            if target==0:
                self.res.append(r)
                return
            for i, v in enumerate(candidates):
                help(candidates[i:], target-v, r+[v])
        help(candidates,target,[])
        return self.res

print(Solution().combinationSum([2, 3, 6, 7], 7))
