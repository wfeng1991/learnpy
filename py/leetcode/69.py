class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        def help(x, guess):
            if abs(x-guess*guess)<1:
                return guess
            else:
                guess=(x/guess+guess)/2
                return help(x, guess)
        return int(help(x,1))

print(Solution().mySqrt(2))