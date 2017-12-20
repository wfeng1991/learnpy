class Solution(object):
    def wordBreak1(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        d=set(''.join(wordDict))
        for c in set(s):
            if c not in d:
                return False
        def help(s,wordDict):
            if not s:
                return True
            for i,w in enumerate(wordDict):
                if s.startswith(w):
                    if help(s[len(w):],wordDict):
                        return True
            return False
        return help(s,sorted(wordDict,key=lambda x:-len(x)))
    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp=[False]*(len(s)+1)
        dp[0]=True
        i=1
        while i<=len(s):
            j=0
            while j<i:
                if dp[j] and wordDict.count(s[j:i]):
                    dp[i]=True
                j+=1
            i+=1
        return dp[-1]

# print(Solution().wordBreak('leetcode',['leet','code']))
print(Solution().wordBreak('a',['a','b']))

# print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
# ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
