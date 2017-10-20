class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        def help(candidates,index,t,target,res):
            if target==0:
                res.append(t)
            elif target<0:
                return
            else:
                i=index
                while i<len(candidates):
                    if i>index and candidates[i]==candidates[i-1]:
                        i+=1
                        continue
                    help(candidates,i+1,t+[candidates[i]],target-candidates[i],res)
                    i+=1
        help(sorted(candidates),0,[],target,res)
        return res

print(Solution().combinationSum2([10,1,2,7,6,1,5],8))