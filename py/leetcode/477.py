class Solution(object):
    def totalHammingDistance1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        i=0
        r=0
        while i<l-1:
            j=i+1
            while j<l:
                t = nums[i] ^ nums[j]
                r += bin(t).count('1')
                j+=1
            i+=1
        return r
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=len(nums)
        i=0
        r=0
        while i<32:
            cnt=0
            j=0
            while j<l:
                cnt+=(nums[j]>>i)&1
                j+=1
            r+=(l-cnt)*cnt
            i+=1
        return r

print(Solution().totalHammingDistance([4,14,2]))