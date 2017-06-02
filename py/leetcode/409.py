class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        dic = {}
        for c in s:
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        r = 0
        for k in dic:
            if dic[k]%2==0:
                r+=dic[k]
            else:
                r+=dic[k]-1
        return r if r==l else r+1