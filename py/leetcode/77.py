class Solution(object):
    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res=[]
        lst=[x for x in range(1,n+1)]
        def help(lst,k,r):
            if k==0:
                self.res.append(r)
            for i,x in enumerate(lst):
                help(lst[i+1:],k-1,r+[x])
        help(lst,k,[])
        return self.res

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k==n or k==0:
            l=[x for x in range(1,k+1)]
            return [l]
        res=self.combine(n-1,k-1)
        res=[x+[n] for x in res]
        res+=self.combine(n-1,k)
        return res

    

print(Solution().combine(20,16))