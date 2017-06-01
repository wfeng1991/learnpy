class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for i, c in enumerate(s):
            if c in dic:
                dic[c][0]=False
            else:
                dic[c]=[True, i]
        r = -1
        for i in dic:
            t = dic[i]
            if t[0]:
                if r==-1 or t[1]<r:
                    r = t[1]
        return r


    def firstUniqChar1(self, s):
        """
        :type s: str
        :rtype: int
        """
        l =len(s)
        for i, c in enumerate(s):
            t = s[0:i]+s[i+1:l]
            if c not in t:
                return i
        return -1

print(Solution().firstUniqChar('lleetcode'))