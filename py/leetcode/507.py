class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<=1:
            return False
        import math
        root = int(math.sqrt(num))+1
        r = 1
        for i in range(2, root):
            if num%i==0:
                r+=i+num//i
        return r==num
        