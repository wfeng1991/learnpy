class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=0
        l=0
        last = True
        for c in s:
            if c=='A':
                a+=1
                last = False
                l=0
            elif (l==0 and c=='L') or (c=='L' and last):
                l+=1
                last = True
            else:
                last = False
                l=0
            if a>1 or l>2:
                return False            
        return True


print(Solution().checkRecord("PLLPLLLLPP"))