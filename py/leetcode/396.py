class Solution(object):
    def maxRotateFunction1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0
        res=-float('inf')
        for i in range(len(A)):
            t=0
            for j,n in enumerate(A[i:]+A[:i]):
                t+=n*j
            res=max(t,res)
        return res

    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        allsum=f=0
        for j,n in enumerate(A):
            f+=j*n
            allsum+=n
        res=f
        for i in range(len(A)-1,0,-1):
            f = f + allsum - len(A) * A[i]
            res = max(f, res)
        return res


print(Solution().maxRotateFunction([-2147483648,-2147483648]))