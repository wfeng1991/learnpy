class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = ''
        tmp = ' '
        for ch in s:
            if ch != ' ':
                tmp += ch
            else:
                l = len(tmp)
                if l > 0:
                    tmp = tmp[::-1]
                    r += tmp
                    tmp = ' '
        if len(tmp) != 0:
            tmp = tmp[1:]
            tmp = tmp[::-1]
            r += tmp
        return r

s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
            