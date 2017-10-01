class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        strs=equation.split('=')
        left=strs[0]
        right=strs[1]
        def help(left):
            p=''
            d=[0,0]
            ll=len(left)
            i=0
            pre='+'
            while i<ll:
                if left[i]=='+' or left[i]=='-':
                    if pre=='+':
                        if p.isdigit():
                            d[1]+=int(p)
                        else:
                            if len(p)>1:
                                d[0]+=int(p[:-1])
                            elif len(p)==1:
                                d[0]+=1
                    else:
                        if p.isdigit():
                            d[1]-=int(p)
                        else:
                            if len(p)>1:
                                d[0]-=int(p[:-1])
                            elif len(p)==1:
                                d[0]-=1
                    pre=left[i]
                    p=''
                else:
                    p+=left[i]
                i+=1
            if pre=='+':
                if p.isdigit():
                    d[1]+=int(p)
                else:
                    if len(p)>1:
                        d[0]+=int(p[:-1])
                    elif len(p)==1:
                        d[0]+=1
            else:
                if p.isdigit():
                    d[1]-=int(p)
                else:
                    if len(p)>1:
                        d[0]-=int(p[:-1])
                    elif len(p)==1:
                        d[0]-=1
            return d
        dl=help(left)
        dr=help(right)
        p=[dl[0]-dr[0],dl[1]-dr[1]]
        if p[0]==0 and p[1]==0:
            return 'Infinite solutions'
        elif p[0]==0:
            return 'No solution'
        else:
            return 'x='+str(-p[1]//p[0])

print(Solution().solveEquation("-x=1"))

        
        