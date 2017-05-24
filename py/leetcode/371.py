# 支持正数
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        r = 0
        mask = 1
        for i in range(0, 32):
            ai = a & mask
            bi = b & mask
            r += ((ai ^ bi + ai & bi) << (ai & bi)) << i
            a >>= 1
            b >>= 1
        return r

print(Solution().getSum(1, 2))

