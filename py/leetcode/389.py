class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l1 = [c for c in s]
        l2 = [c for c in t]
        for c in l1:
            l2.remove(c)
        return l2[0]

print(Solution().findTheDifference("asa", "asac"))        
        
