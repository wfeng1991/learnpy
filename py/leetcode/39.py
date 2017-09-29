class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def help(candidates, target, t, res):
            if target<0:
                return
            if target==0:
                res.append(t)
                return
            for i, v in enumerate(candidates):
                help(candidates[i:], target-v, t+[v], res)
        help(candidates,target,[],res)
        return res

print(Solution().combinationSum([2, 3, 6, 7], 7))
