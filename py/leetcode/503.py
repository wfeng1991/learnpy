class Solution(object):
    def nextGreaterElements1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=len(nums)
        r=[]
        i=0
        while i<l:
            j=i+1
            t=-1
            while j<l+i:
                if nums[j%l]>nums[i]:
                    t=nums[j%l]
                    break
                j+=1
            r.append(t)
            i+=1
        return r
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        s=[]
        l=len(nums)
        r=[-1]*l
        i=2*l-1
        while i>=0:
            while len(s)>0 and s[-1]<=nums[i%l]:
                s.pop()
            if len(s)!=0:
                r[i%l]=s[-1]
            s.append(nums[i%l])
            i-=1
        return r
print(Solution().nextGreaterElements([1,2,3,2,1]))
        