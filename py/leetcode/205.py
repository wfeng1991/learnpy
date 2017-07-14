class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        def pattern(s):
            dt = dict()
            cur=1
            pt = ''
            for c in s:
                if c in dt:
                    pt+=dt[c]
                else:
                    dt[c]=str(cur)
                    pt+=str(cur)
                    cur+=1
            return pt
        return pattern(s)==pattern(t)
print(Solution().isIsomorphic('foo','boo'))
        