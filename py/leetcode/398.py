class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        :type numsSize: int
        """
        self.n=nums
        import random
        self.r=random.Random()
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        c=0
        r=-1
        for i,n in enumerate(self.n):
            if n!=target:
                continue
            if self.r.randint(0,c)==0:
                r=i
                c=1
        return r


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)