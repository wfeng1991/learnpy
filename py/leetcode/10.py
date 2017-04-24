class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '':
            return s == ''
        elif len(p)==1:
            return len(s)==1 and (s[0]==p[0] or p[0] == '.')

        if '*' == p[1]:
            if len(p) >= 2:
                return self.isMatch(s, p[2:]) or (len(s)!=0 and (s[0]==p[0] or p[0] == '.') and self.isMatch(s[1:], p))
            else:
                return (len(s)!=0 and (s[0]==p[0] or p[0] == '.') and self.isMatch(s[1:], p))
        else:
            return len(s)!=0 and (s[0]==p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])

s = Solution()
s = s.isMatch('aa', 'a*')
print(s)

        