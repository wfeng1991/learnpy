class Solution(object):
    def predictPartyVictory1(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        stack=[c for c in senate][::-1]
        R=stack.count('R')
        D=stack.count('D')
        r,d=0,0
        while len(stack)>1:
            if R==len(stack):
                return 'Radiant'
            if D==len(stack):
                return 'Dire'
            t=stack.pop()
            while t=='R' and r>0:
                t=stack.pop()
                r-=1
                R-=1
            while t=='D' and d>0:
                t=stack.pop()
                d-=1
                D-=1
            if t=='R':
                d+=1
            else:
                r+=1
            stack=[t]+stack
        return 'Radiant' if stack[0]=='R' else 'Dire'

    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        R,D=[],[]
        for i,c in enumerate(senate):
            if c=='R':
                R.append(i)
            else:
                D.append(i)
        l=len(senate)
        while len(R) and len(D):
            r,d=R[0],D[0]
            if r<d:
                R=R[1:]+[r+l]
                D=D[1:]
            else:
                R=R[1:]
                D=D[1:]+[d+l]
        return 'Radiant' if len(R) > len(D) else 'Dire'


print(Solution().predictPartyVictory("RDR"))
            
            