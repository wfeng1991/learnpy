class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        ll = len(word)
        if ll < 2:
            return True

        l = map(chr, range(65, 91))
        if word[0] in l:
            for i in range(2, ll):
                if word[1] in l and word[i] not in l:
                    return False
                elif word[1] not in l and word[i] in l:
                    return False
        else:
            for i in range(1, ll):
                if word[i] in l:
                    return False
        return True

print(Solution().detectCapitalUse("uZfa"))