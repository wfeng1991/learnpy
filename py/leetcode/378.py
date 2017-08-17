class Solution(object):
    def kthSmallest1(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        idxs=[0 for i in range(0,n)]
        i=1
        while i<=k:
            j=-1
            current=float('inf')
            for q,p in enumerate(idxs):
                if p<n and matrix[q][p]<current:
                    current=matrix[q][p]
                    j=q
            idxs[j]+=1
            i+=1
        return current
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n=len(matrix)
        lo=matrix[0][0]
        hi=matrix[-1][-1]+1
        while lo<hi:
            cnt=0
            mid=(lo+hi)//2
            for i in range(n):
                j=len(matrix[i])-1
                while j>=0 and matrix[i][j]>mid:
                    j-=1
                cnt+=j+1
            if cnt<k:
                lo=mid+1
            else:
                hi=mid
        return lo
print(Solution().kthSmallest([
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],8))