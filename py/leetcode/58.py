class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        if l==0:
            return 0
        i=l-1
        cnt=0
        while i>=0:
            if s[i]==' ':
                i-=1
            else:
                break
        while i>=0:
            if s[i]!=' ':
                cnt+=1
                i-=1
            else:
                break
        return cnt

print(Solution().lengthOfLastWord('Hello World'))  