class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums)<2:
            return
        i=len(nums)-1
        while i>0 and nums[i-1]>=nums[i]:
            i-=1
        if i==0:
            while p<q:
                nums[p],nums[q]=nums[q],nums[p]
                p+=1
                q-=1
        else:
            j=i-1
            p=len(nums)-1
            while p>j and nums[p]<=nums[j]:
                p-=1
            nums[j],nums[p]=nums[p],nums[j]
            nums[i:]=sorted(nums[i:])
        print(nums)

Solution().nextPermutation([3,2,1])