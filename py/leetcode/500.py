class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r1 = 'qwertyuiopQWERTYUIOP'
        r2 = 'asdfghjklASDFGHJKL'
        r3 = 'zxcvbnmZXCVBNM'
        i = r1
        l = len(words)-1
        while l>=0:
            new = True
            for c in words[l]:
                if new:
                    new = False
                    if r1.find(c)!=-1:
                        i = r1
                    elif r2.find(c)!=-1:
                        i = r2
                    else:
                        i = r3
                else:
                    if words[l] in words and i.find(c)==-1:
                        words.remove(words[l])
                        break
            l -= 1
        return words

s = Solution()
print(s.findWords(["Hello","Alaska","Dad","Peace"])) 
                