class NumArray(object):



    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.data=nums
        self.cache=dict()
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        key=str(i)+str(j)
        if key in self.cache:
            return self.cache[key]
        else:
            sums = sum(self.data[i:j+1])
            self.cache[key]=sums
            return sums

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)