class Solution(object):
    def getPermutation1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        s=''.join([str(i) for i in range(1,n+1)])
        self.n=0
        self.res=s
        def permutation(s,tmp,k):
            if not s:
                self.n+=1
                if self.n==k:
                    self.res=tmp
            for i,c in enumerate(s):
                permutation(s[:i]+s[i+1:],tmp+c,k)
        permutation(s,'',k)
        return self.res

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res=''
        nums=[str(i) for i in range(1,n+1)]
        while len(res)<n:
            p,t=len(nums)-1,1
            while p>0 and t*p<=k:
                t*=p
                p-=1
            if p>=1:
                res+=nums[0]
                nums.pop(0)
            else:
                q=k//t-1 if k%t==0 else k//t
                res+=nums[q]
                nums.pop(q)
                k=k-q*t
        return res


print(Solution().getPermutation(9,5040))