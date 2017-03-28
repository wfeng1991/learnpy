class Solution(object):
    def myAtoi(self, str):
        i = 0
        sign = True
        for c in str:
            if c == '-':
                sign =False
            if c == '.':
                break
            if c.isdigit():
                i = i * 10 + int(c)
        if not sign:
            i = -1 * i 
        return i
            
s = Solution()
s = s.myAtoi('21321.12212')
print(s)