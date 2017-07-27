class Solution(object):
    def countSubstrings1(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        if l<2:
            return l
        def palindrom(s):
            l=len(s)
            i,j=0,l-1
            f=True
            while i<j:
                if s[i]!=s[j]:
                    f=False
                i+=1
                j-=1
            return f
        i=1
        cnt=0
        while i<=l:
            j=0
            while j+i<=l:
                if palindrom(s[j:j+i]):
                    cnt+=1
                j=j+1
            i+=1
        return cnt


    def countSubstrings(self, S):
        N = len(S)
        ans = 0
        for center in range(0,2*N - 1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < N and S[left] == S[right]:
                ans += 1
                left -= 1
                right += 1
        return ans

print(Solution().countSubstrings('aaa'))