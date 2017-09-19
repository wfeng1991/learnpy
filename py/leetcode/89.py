class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        m = 1<<n
        r=[]
        for i in range(m):
            r.append(i^(i>>1))
        return r

print(Solution().grayCode(10))

