class Solution(object):
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        nums[:] = nums[-k:]+nums[:l-k]

    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l=len(nums)
        k=k%l
        s=0
        m1=l-k-1
        m2=m1+1
        e=l-1
        while s<m1:
            nums[s],nums[m1]=nums[m1],nums[s]
            s+=1
            m1-=1
        while m2<e:
            nums[e],nums[m2]=nums[m2],nums[e]
            m2+=1
            e-=1
        e=l-1
        s=0
        while s<e:
            nums[s],nums[e]=nums[e],nums[s]
            s+=1
            e-=1
        print(nums)

Solution().rotate([1,2],1)