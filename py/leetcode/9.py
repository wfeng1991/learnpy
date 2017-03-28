class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            x = -x
        s = str(x)
        l = len(s)
        for i,c in enumerate(s):
            if i < l//2:
                if c != s[l-1-i]:
                    return False
        return True


x = Solution()
x = x.isPalindrome(-2147447412)
print(x)