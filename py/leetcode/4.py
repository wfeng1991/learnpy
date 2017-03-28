class Solution(object):
    def findMedianSortedArrays(self, arr1, arr2):
        length = len(arr1) + len(arr2)
        k = length // 2
        if length % 2 == 0:
            aa = self.findK(arr1, arr2, 0, len(arr1)-1, 0, len(arr2)-1, k)
            bb = self.findK(arr1, arr2, 0, len(arr1)-1, 0, len(arr2)-1, k+1)
            return (aa+bb)/2
        else:
            aa = self.findK(arr1, arr2, 0, len(arr1)-1, 0, len(arr2)-1, k+1)
            return aa

    def findK(self, arr1, arr2, s1, e1, s2, e2, k):
        if len(arr1) == 0:
            return arr2[k-1]
        length1 = e1 - s1 + 1
        length2 = e2 - s2 + 1
        if length1 > length2:
            return self.findK(arr2, arr1, s2, e2, s1, e1, k)
        if length1 == 0:
            return arr2[k-1]
        else:
            if k == 1:
                if arr1[s1] > arr2[s2]:
                    return arr2[s2]
                else:
                    return arr1[s1]
        pos1 = k // 2
        if length1 < pos1:
            pos1 = length1
        pos2 = k - pos1
        pos1 = pos1 + s1
        pos2 = pos2 + s2
        if arr1[pos1-1] > arr2[pos2-1]:
            return self.findK(arr1, arr2, s1, e1, pos2, e2, k - pos2 + s2)
        elif arr1[pos1-1] < arr2[pos2-1]:
            return self.findK(arr1, arr2, pos1, e1, s2, e2, k - pos1 + s1)
        else:
            return arr2[pos2-1]
        
key = Solution()
key = key.findMedianSortedArrays([1,2], [3,4])
print(key)


