class Solution:
    def multiply1(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return '0'
        def mul(num,d):
            res=''
            carry=0
            for n in num[::-1]:
                t=int(n)*int(d)+carry
                res=str(t%10)+res
                carry=t//10
            return str(carry)+res if carry>0 else res
        def add(m,n):
            if len(m)>len(n):
                n=n.rjust(len(m),'0')
            else:
                m=m.rjust(len(n),'0')
            res=''
            i=len(m)-1
            carry=0
            while i>=0:
                t=int(n[i])+int(m[i])+carry
                res=str(t%10)+res
                carry=t//10
                i-=1
            return str(carry)+res if carry>0 else res
        res='0'
        for i,n in enumerate(num1[::-1]):
            res=add(mul(num2,n)+'0'*i,res)
        return res

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1=='0' or num2=='0':
            return '0'
        res=[0]*(len(num1)+len(num2))
        for i,n in enumerate(num1[::-1]):
            for j,m in enumerate(num2[::-1]):
                t=int(n)*int(m)+res[i+j]
                res[i+j] = t % 10;
                res[i+j+1] += t//10;
        return ''.join(map(str,res))[::-1].lstrip('0')



print(Solution().multiply('14','15'))
             