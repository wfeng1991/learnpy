class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]
        import sys
        count = ''
        l = sys.float_info.max
        for x in strs:
            if l > len(x):
                l = len(x)
        if l == 0:
            return count
        for i in range(0, l):
            c = strs[0][i]
            f = True
            for x in strs:
                if c != x[i]:
                    f = False
                    break
            if f:
                count = count + c
            else:
                return count
        return count
        

s = Solution()
s = s.longestCommonPrefix(["c","c"])
print(s)