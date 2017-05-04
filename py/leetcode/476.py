class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = 1
        idx = 31
        f = False
        while idx >= 0:
            t = num >> idx
            if not f and t & mask == 0:
                idx -= 1
                continue
            elif not f and t & mask == 1:
                f = True
                m = mask << idx
                num = num ^ m
                idx -= 1
            else:
                m = mask << idx
                num = num ^ m
                idx -= 1
        return num

s = Solution()
print(s.findComplement(1))