class Solution(object):
    def lengthOfLIS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        if l<2:
            return l
        k=[1]*l
        m=1
        i=1
        while i<l:
            j=i
            t=0
            while j>=0:
                if nums[i]>nums[j]:
                    t=max(t,k[j])
                j-=1
            k[i]+=t
            m=max(k[i],m)
            i+=1
        return m

    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                m = (i + j) / 2
                if tails[m] < x:
                    i = m + 1
                else:
                    j = m
            tails[i] = x
            size = max(i + 1, size)
        return size

print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
