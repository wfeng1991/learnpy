class Solution:
    def find132pattern1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        if l<3:
            return False
        s3=-float('inf')
        i=l-1
        while i>=0:
            if i>0 and nums[i-1]>nums[i]:
                s3=max([x for x in nums[i:] if x<nums[i-1]])
                if i-2>=0 and nums[i-2]<s3:
                    return True
            elif nums[i]<s3:
                return True
            i-=1
        return False

    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=len(nums)
        if l<3:
            return False
        stack=[]
        s3=-float('inf')
        i=l-1
        while i>=0:
            if nums[i]<s3:
                return True
            while stack and nums[i]>stack[-1]:
                s3=stack.pop()
            stack.append(nums[i])       
            i-=1
        return False


print(Solution().find132pattern([3,5,0,4,4]))
                
            