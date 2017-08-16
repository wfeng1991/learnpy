class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.r=[]
        def help(k,n,t,p):
            if n==0 and k==0:
                self.r.append(p)
            for i,v in enumerate(t):
                help(k-1,n-v,t[i+1:],p+[v])
        help(k,n,list(range(1,10)),[])
        return self.r

print(Solution().combinationSum3(5,25))