class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        l1 = len(nums1)
        l2 =len(nums2)
        r = []
        nums1.sort()
        nums2.sort()
        i = 0
        j = 0
        while j<l2 and i<l1:
            if nums1[i]==nums2[j]:
                r.append(nums1[i])
                j+=1
                i+=1
            elif nums1[i]>nums2[j]:
                j+=1
            else:
                i+=1
        return r
            
