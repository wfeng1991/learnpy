class Solution(object):
    def reverse(self, x):
        lesszero = False
        if x < 0:
            x = -x
            lesszero = True
        r = 0
        while x % 10 != 0 or x > 0:
            y = x % 10 
            r = r*10 + y*10
            x = x // 10
        if r//10 - 2147483647 > 0:
            return 0
        if lesszero:
            r = r //10 * -1
        else:
            r = r //10
        return r

res = Solution()
res = res.reverse(-2147483412)
print(res)
