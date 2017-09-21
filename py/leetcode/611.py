class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def binsearsh(nums,s,e,t):
            while e >= s and e < len(nums):
                mid = (s + e) // 2
                if nums[mid] >= t:
                    e = mid - 1
                else:
                    s = mid + 1
            return s
        
        l = len(nums)
        nums=sorted(nums)
        i=0
        r=0
        while i<l:
            j=i+1
            while j<l:
                p=binsearsh(nums,j+1,l-1,nums[i]+nums[j])
                r+=p-j-1
                j+=1
            i+=1
        return r

print(Solution().triangleNumber([2,2,3,4]))

        