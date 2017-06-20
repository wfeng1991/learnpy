class Solution(object):

    # 递归方法容易理解 但是时间复杂是指数增长
    def climbStairs0(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cnt=0
        def walk(n):
            if n==0:
                self.cnt+=1
                return       
            if n>1:                         
                walk(n-1) or walk(n-2)
            else:
                walk(n-1)
        walk(n)
        return self.cnt
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        t = [1,1]
        i = 1
        while i<n:
            t[i%2]=t[1]+t[0]
            i+=1
        return t[(i-1)%2]
        
print(Solution().climbStairs(6))