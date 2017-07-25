class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return 9
        m=pow(10,n)-1
        n=m//10
        t=m
        while m>n:
            p=int(str(m)+str(m)[::-1])
            tt=t
            while tt*tt>=p:
                if p%tt==0:
                    return p%1337
                tt-=1
            m-=1
        return 0
print(Solution().largestPalindrome(8))