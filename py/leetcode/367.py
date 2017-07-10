class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<0:
            return False
        if num==0 or num==1:
            return True
        def sqrt(x,g):
            if abs(g*g-x)<0.1:
                return g
            else:
                return sqrt(x,(x/g+g)/2)
        root = round(sqrt(num,1))
        if root*root==num:
            return True
        return False

print(Solution().isPerfectSquare(5))
        