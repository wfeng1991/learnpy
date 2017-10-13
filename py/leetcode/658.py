class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]
        i, j = 0, len(arr)
        while j-i>1:
            mid = (i + j) // 2
            if arr[mid] > x:
                j = mid - 1
            else:
                i = mid
        low,high=max(0,i-k+1),min(len(arr)-1,i+k-1)
        while high-low>=k:
            if x-arr[low]<=arr[high]-x:
                high-=1
            else:
                low+=1
        return arr[low:high+1]

print(Solution().findClosestElements([0,1,2,2,2,3,6,8,8,9],5,9))