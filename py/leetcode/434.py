class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt=0
        pre=None
        l=len(s)-1
        for i,c in enumerate(s):
            if c!=' ':
                pre=c
            if (pre and c==' ') or (i==l and pre):
                pre=None
                cnt+=1
        return cnt


print(Solution().countSegments('Hello, my name is John'))

