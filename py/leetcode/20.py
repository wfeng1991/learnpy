class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False
        r = []
        for p in s:
            if p == '(' or p == '[' or p == '{':
                r.append(p)
            else:
                if len(r) == 0:
                    return False
                m = r.pop()
                if (m == '(' and p == ')') or (m == '[' and p == ']') or (m == '{' and p == '}'):
                    continue
                else:
                    return False
        return len(r) == 0


s = Solution()
print(s.isValid('(('))