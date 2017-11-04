class Solution(object):
    def countBinarySubstrings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        i=0
        cnt=0
        while i<len(s):
            j=i+1
            while j<len(s):
                f=True
                p,q=i,j
                while p<q:
                    if s[p]==s[i] and s[q]==s[j] and s[p]!=s[q]:
                        p+=1
                        q-=1
                    else:
                        f=False
                        break
                if f:cnt+=1
                j+=2
            i+=1
        return cnt

    def countBinarySubstrings(self, s):
        ans, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i-1] != s[i]:
                ans += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return ans + min(prev, cur)
print(Solution().countBinarySubstrings('00110'))