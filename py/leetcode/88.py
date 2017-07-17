class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n==0:
            return
        i=0
        j=m
        while i<n:
            nums1[j]=nums2[i]
            i+=1
            j+=1
        p,q=0,m
        if p==q:
            return
        while p<m:
            if nums1[p]>nums1[q]:
                nums1[p],nums1[q]=nums1[q],nums1[p]
                p+=1
                t=q
                while t+1<m+n:
                    if nums1[t]>nums1[t+1]:
                        nums1[t],nums1[t+1]=nums1[t+1],nums1[t]
                    t+=1
            else:
                p+=1
        print(nums1)
        
Solution().merge([1,2,3,0,0,0],3,[2,5,6],3)
        
