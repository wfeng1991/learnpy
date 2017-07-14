class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strArr=str.split(' ')
        if len(pattern)!=len(strArr):
            return False
        dic = dict()
        l = len(pattern)
        for i in range(0,l):
            if pattern[i] not in dic and strArr[i] not in dic.values():
                dic[pattern[i]]=strArr[i]
            else:
                if pattern[i] not in dic or dic[pattern[i]]!=strArr[i]:
                    return False
        return True

print(Solution().wordPattern('abba','dog c c d'))