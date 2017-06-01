class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        l = len(ops)
        if l==0:
            return m*n
        r=[m, n]
        for p in ops:
            row = p[0]
            col = p[1]
            r[0]=min(row,r[0])
            r[1]=min(col,r[1])
        return r[0]*r[1]

print(Solution().maxCount(3,3,[[2,2],[3,3]]))