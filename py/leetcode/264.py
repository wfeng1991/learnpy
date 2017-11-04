class Solution(object):
    def nthUglyNumber1(self, n):
        """
        :type n: int
        :rtype: int
        """
        factors=[2,3,5]
        nums=[1]
        while len(nums)<n:
            t=min([x*y for x in nums for y in factors if x*y>nums[-1]])
            nums.append(t)
        return nums[-1]

    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums=[1]*n
        f2=f3=f5=0
        i=1
        while i<n:
            nums[i]=min(nums[f2]*2,nums[f3]*3,nums[f5]*5)
            if nums[f2]*2==nums[i]:f2+=1
            if nums[f3]*3==nums[i]:f3+=1
            if nums[f5]*5==nums[i]:f5+=1
            i+=1
        return nums[-1]