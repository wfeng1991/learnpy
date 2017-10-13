class Solution(object):

    def longestSubstring1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxlen = 0
        l = len(s)
        i = 0
        while i < l:
            j = l
            while j >= i + k:
                t = s[i:j]
                f = True
                for c in set(t):
                    if t.count(c) < k:
                        f = False
                        break
                if f:
                    maxlen = max(maxlen, j - i)
                j -= 1
            i += 1
        return maxlen

    def longestSubstring(self, s, k):
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

print(Solution().longestSubstring("bbaaacbd", 3))
