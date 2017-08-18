class Solution(object):
    def maxProduct1(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        i=0
        m=0
        while i<len(words):
            j=i+1
            while j<len(words):
                f=True
                for c in words[i]:
                    if c in words[j]:
                        f=False
                        break
                if f:
                    m=max(m,len(words[i])*len(words[j]))
                j+=1
            i+=1
        return m
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        if not words:
            return 0
        v=[0 for i in range(len(words))]
        for i,w in enumerate(words):
            for c in w:
                v[i] |= 1<<ord(c)-ord('a')
        m=0
        i=0
        while i<len(words):
            j=i+1
            while j<len(words):
                if v[i]&v[j]==0: 
                    m=max(m,len(words[i])*len(words[j]))
                j+=1
            i+=1
        return m

print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))