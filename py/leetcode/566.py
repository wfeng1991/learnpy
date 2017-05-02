class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        res = []
        rr = len(nums)
        cc = len(nums[0])
        if cc*rr != r*c:
            return nums
        t = []
        k = 0
        for l in nums:
            for n in l:
                if k < c:
                    k += 1
                    t.append(n)
                else:
                    res.append(t)
                    t = []
                    k = 1
                    t.append(n)
                    
        if t != []:
            res.append(t)
        return res
    
s = Solution()
print(s.matrixReshape([[1,2],[3,4]], 1, 4))
