class Solution(object):
    def lastRemaining1(self, n):
        """
        :type n: int
        :rtype: int
        """
        t=list(range(1,n+1))
        start=True
        while len(t)!=1:
            p=[]
            if start:
                for i,n in enumerate(t):
                    if i%2==1:
                        p.append(n)
                t=p
                start=False
            else:
                j=len(t)
                while j-2>=0:
                    p=[t[j-2]]+p
                    j-=2
                t=p
                start=True
        return t[0]
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        left=True
        start=1
        step=1
        remaining=n
        while remaining>1:
            if left or remaining%2==1:
                start+=step
            remaining /= 2
            step *= 2
            left = not left
        return start
            
print(Solution().lastRemaining(9))