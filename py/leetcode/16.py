class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        length = len(nums)-1
        small = nums[0]+nums[1]+nums[2]
        large = nums[length-2]+nums[length-1]+nums[length]

        if large <= target:
            return large
        elif small >= target:
            return small
        else:
            if self.threeSum(nums, length, target):
                return target
            sum = large if abs(target-large) < abs(target-small) else small
            between = min(abs(target-large), abs(target-small))
            i = 1
            while i < between:
               if self.threeSum(nums, length, target - i):
                  if between > i:
                     sum = target - i
                     between = i
               if self.threeSum(nums, length, target + i):
                   if between > i:
                     sum = target + i
                     between = i
               i = i + 1
            return sum

    def threeSum(self, nums, length, target):
        """
        :type sorted nums: List[int]
        :type target: int
        :rtype: int
        """
        l = length
        j = 0
        while j < l-2:
            i = j+1
            low = i 
            high = l
            while low < high:
                t = target - nums[j]
                if t == nums[low] + nums[high]:
                    return True
                elif t > nums[low] + nums[high]:
                    low = low+1
                else:
                    high = high-1
            j = j+1
        return False

s = Solution()
print(s.threeSumClosest([1,2,4,8,16,32,64,128],82))

