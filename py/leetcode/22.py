class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        r = []
        self.helper(r, '', n, n)
        return r

    def helper(self, r, s, left, right):
        if left == 0 and right == 0:
            r.append(s)
        if left > 0:
            self.helper(r, s+'(', left-1, right)
        if right > 0 and right > left:
            self.helper(r, s+')', left, right-1)

s = Solution()
print(s.generateParenthesis(2))
