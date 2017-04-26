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
            if s == 0 or (s > 0 and nums[s] != nums[s - 1]):
                i = nums[s]
                if i > 0:
                    break
                a = s + 1
                l = length
                sum = -i
                while a < l:
                    if nums[a] + nums[l] == sum:
                        t = [i, nums[a], nums[l]]
                        r.append(t)
                        while a < l and nums[a] == nums[a+1]:
                            a = a + 1
                        while a < l and nums[l] == nums[l-1]:
                            l = l - 1                        
                        l = l - 1
                        a = a + 1
                    elif a < l and nums[a] + nums[l] > sum:
                        l = l - 1
                    else:
                        a = a + 1
            s = s+1
        return r

s = Solution()
print(s.threeSum([1,-1,-1,0]))
