class Solution(object):
    '''
        错误答案
    '''
    def reverseStr1(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        def reverse(s, start, end):
            l = [c for i,c in enumerate(s) if start<=i<end]
            mid = (end - start)//2
            length=end-start-1
            i=0
            while i<mid:
                t = l[i]
                l[i] = l[length-i]
                l[length-i] = t
                i+=1
            r=''
            for c in l:
                r+=c
            return r

        l = len(s)
        if l<=k:
            return reverse(s,0,l)
        else:
            i=1
            res = ''
            while l-k*i>0:
                res += reverse(s,k*i-k,k*i)
                i+=1
            if l>k*i-k:
                res += reverse(s,k*i-k,l)
            return res

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        res = ''
        start = 0
        l = len(s)
        while l-start>0:
            p = start+k-1 if start+k-1<l else l-1
            while p>=start:
                res += s[p]
                p-=1
            p = start+k
            while p<start+2*k and p < l:
                res += s[p]
                p+=1
            start += 2*k
        return res
        
            
print(Solution().reverseStr('abcdefg',2))
