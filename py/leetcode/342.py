class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        if num<4:
            return False
        idx=1
        mask=3
        while idx<16 and num>0:
            if mask&num==0:
                num=num>>(idx*2)
            elif num==1:
                return True
            else:
                return False
        