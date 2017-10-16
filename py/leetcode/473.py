class Solution(object):
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        t=sum(nums)
        if t==0:
            return False
        if t%4!=0:
            return False
        edge=t//4
        sums=[0]*4
        nums=sorted(nums,key=lambda x:-x)
        def help(nums,sums,index,edge):
            if index==len(nums):
                if sums[0]==sums[1]==sums[2]==edge:
                    return True
                return False
            for i in range(4):
                if sums[i]+nums[index]>edge:
                    continue
                sums[i]+=nums[index]
                if help(nums,sums,index+1,edge):
                    return True
                sums[i]-=nums[index]
            return False
        return help(nums,sums,0,edge)

print(Solution().makesquare([2,2,2,3,4,4,4,5,6]))