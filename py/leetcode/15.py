class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        r = []
        length = len(nums)-1
        if length < 2:
            return []
        nums = sorted(nums)
        s = 0
        while s < length: 
            i = nums[s]
            if i > 0:
                break
            a = s + 1
            l = length
            while a < l:
                if nums[a]+nums[l]>-i:
                    l = l - 1
                elif nums[a]+nums[l]<-i:
                    a = a + 1
                else: 
                    t = [i, nums[a], nums[l]]            
                    if t not in r:
                        r.append(t)
                    l = l - 1
                    a = a + 1                 
            s = s+1
        return r

s = Solution()
print(s.threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))