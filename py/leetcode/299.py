class Solution(object):
    def getHint1(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A=[]
        B=[]
        for k in range(len(guess)):
            if k not in A and guess[k]==secret[k]:
                A.append(k)
                B.append(k)
        al=len(A)    
        for k,s in enumerate(secret):
            if k not in B:
                for _k,g in enumerate(guess):
                    if _k not in A and k not in B and s==g:
                        B.append(k)
                        A.append(_k) 
        return str(al)+'A'+str(len(B)-al)+'B'

    def getHint2(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        a=0
        for k in range(len(guess)):
            if guess[k]==secret[k]:
                a+=1
        guess=sorted(guess)
        secret=sorted(secret)
        dp=[[0]*(len(guess)+1) for _ in range(len(secret)+1)]
        for i,s in enumerate(secret):
            for j,g in enumerate(guess):
                if s==g:
                    dp[i+1][j+1]=dp[i][j]+1
                else:
                    dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
        b=dp[-1][-1]-a
        return str(a)+'A'+str(b)+'B'

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        s={}
        for c in secret:
            s[c]=s.get(c,0)+1
        g={}
        for c in guess:
            g[c]=g.get(c,0)+1
        a=0
        for k in range(len(guess)):
            t=guess[k]
            if t==secret[k]:
                a+=1
                s[t]-=1
                g[t]-=1
        b=0
        for k in guess:
            if g[k]>0 and k in s and s[k]>0:
                b+=1
                g[k]-=1
                s[k]-=1
        return str(a)+'A'+str(b)+'B'
        

print(Solution().getHint("12", "23"))



        