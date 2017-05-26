class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i=0
        j=len(numbers)-1
        while j>i:
            if numbers[i]+numbers[j]>target:
                j=j-1
            elif numbers[i]+numbers[j]<target:
                i=i+1
            else:
                return [i+1,j+1]

print(Solution().twoSum([0,0,3,4],0))