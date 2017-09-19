class Solution(object):
    def lexicalOrder1(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l=[x for x in range(1,n+1)]
        return sorted(l,key=lambda x:str(x))
        
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        r=[]
        cur=1
        while cur<=n and len(r)<n:
            r.append(cur)
            if cur*10<=n:
                cur*=10
            elif cur%10!=9 and cur+1<=n:
                cur+=1
            else:
                while (cur//10)%10==9:
                    cur//=10
                cur=cur//10+1
        return r    

print(Solution().lexicalOrder(13))
