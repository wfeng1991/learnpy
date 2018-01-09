class Solution:
    def canJump1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def help(nums,idx,step):
            if (len(nums)-1-idx)<=step:
                return True
            for i in range(step,0,-1):
                if nums[idx+i] and help(nums,idx+i,nums[idx+i]):
                    return True
            return False
        return help(nums,0,nums[0])

    def canJump2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        stack=[[0,s] for s in range(1,nums[0]+1)]
        while stack:
            idx,step=stack.pop()
            if (len(nums)-1-idx)<=step:
                return True
            stack+=[[idx+s,nums[idx+s]] for s in range(1,step+1) if nums[idx+s]!=0]
        return False

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        last_good_index=len(nums)-1
        p=last_good_index-1
        while p>=0:
            if nums[p]+p>=last_good_index:
                last_good_index=p
            p=p-1
        return last_good_index==0
# print(Solution().canJump([3,2,1,0,4])) 
print(Solution().canJump([1,1,2,2,0,1,1])) 