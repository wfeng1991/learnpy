class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        n=[]
        t=''
        for c in expression:
            if c=='+' or c=='-':
                if len(t)>0:
                    n.append(t)
                t=''
            t+=c
        if t:
            n.append(t)
        from functools import reduce
        def sumf(x,y):
            a,b=x.split('/')
            c,d=y.split('/')
            t1=int(a)*int(d)+int(c)*int(b)
            t2=int(b)*int(d)
            return str(t1)+'/'+str(t2)
        r = reduce(sumf,n)
        def gcd(x,y):
            if y==0:
                return x
            elif x==0:
                return y
            t=x%y
            if t:
               return gcd(y,t)
            return y
        t=r.split('/')
        p=gcd(abs(int(t[0])),int(t[1]))
        if p!=-1 and p!=1:
            r=str(int(t[0])//p)+'/'+str(int(t[1])//p)
        return r

    
print(Solution().fractionAddition("-4/7-3/4+2/3"))

            
