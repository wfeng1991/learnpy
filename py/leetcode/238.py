class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=1
        zero=[]
        for i,v in enumerate(nums):
            if v!=0:
                s*=v
            else:
                zero.append(i)
        if len(zero)>1:
            return [0]*len(nums)
        r=[]
        for i,v in enumerate(nums):
            if len(zero)==0:
                r.append(s//v)
            else:
                if i==zero[0]:
                    r.append(s)
                else:
                    r.append(0)
        return r

print(Solution().productExceptSelf([1,0]))