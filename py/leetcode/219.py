class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        l = len(nums)
        if l<2:
            return False
        dic = dict()
        for i,n in enumerate(nums):
            if n in dic and abs(dic[n]-i)<=k:
                return True
            else:
                dic[n]=i
        return False