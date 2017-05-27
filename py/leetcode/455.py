class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g = sorted(g)
        s = sorted(s)
        cnt=0
        j=0
        l =len(s)
        i=0
        while i<len(g):          
            while j<l and g[i]>s[j]:
                j+=1
            if j<l:
                cnt += 1
            else:
                break
            j+=1
            i+=1
        return cnt

print(Solution().findContentChildren([1,3],[1,2]))
                
