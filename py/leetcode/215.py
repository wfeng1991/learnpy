class Solution(object):

    def findKthLargest1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, key=lambda x: -x)[k - 1]

    # use partition
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def partition(nums, low, high):
            l = low
            h = high
            k = nums[l]
            while l < h:
                while l < h and k >= nums[h]:
                    h -= 1
                if h > l:
                    nums[l] = nums[h]
                    l += 1
                while l < h and k <= nums[l]:
                    l += 1
                if l < h:
                    nums[h] = nums[l]
                nums[l] = k
            return l
        l = len(nums)
        i, j = 0, l - 1
        while i < j:
            p = partition(nums, i, j)
            if p < k-1:
                i = i + 1
            elif p > k-1:
                j = j - 1
            else:
                return nums[p]
        return nums[k-1]

print(Solution().findKthLargest([1,2,4,5,6,453,4,100],2))
