class Solution(object):
    def findUnsortedSubarray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def findsub(nums):
            if len(nums)==0:
                return 0
            if nums[0]==min(nums):
                return findsub(nums[1:])
            if nums[-1]==max(nums):
                return findsub(nums[:-1])
            return len(nums)
        return findsub(nums)
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        snums=sorted(nums)
        s=0
        e=len(nums)-1
        i=0
        while i<len(nums):
            i+=1
            if nums[s]==snums[s]:
                s+=1
            if nums[e]==snums[e]:
                e-=1
        if s>=e:
            return 0 
        else:
            return e-s+1
print(Solution().findUnsortedSubarray([1,2,0,3,4,5,6,7,8,9]))
        
