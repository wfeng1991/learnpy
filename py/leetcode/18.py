class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        r = []
        length = len(nums) - 1
        if length < 3:
            return r
        nums = sorted(nums)
        idx = 0
        j = length
        while idx <= j and j - idx > 0:
            first = nums[idx]
            t = target - first
            idx3 = idx + 1
            p = idx3
            while p <= length:
                k = length
                second = nums[p]
                idx3 = p
                tt = t - second
                while idx3 <= k and k - idx3 > 0:
                    if idx3 + 1 < k and tt == nums[idx3 + 1] + nums[k]:
                        sr = [first, second, nums[idx3 + 1], nums[k]]
                        if sr not in r:
                            r.append(sr)
                        while idx3 + 2<=k and nums[idx3 + 1] == nums[idx3 + 2]:
                            idx3 = idx3 + 1
                        while k-1>=idx3 and nums[k] == nums[k - 1]:
                            k = k - 1
                        idx3 = idx3 + 1
                        k = k - 1
                    elif tt > nums[idx3 + 1] + nums[k]:
                        idx3 = idx3 + 1
                    else:
                        k = k - 1
                p = p + 1
            idx = idx + 1
        return r
sss = Solution()
# print(sss.fourSum([1, 0, -1, 0, -2, 2], 0))
print(sss.fourSum([-3,-2,-1,0,0,1,2,3], 0))
