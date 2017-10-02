class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        p=[int(c) for c in str(num)]
        l=len(p)
        k=0
        while k<l:
            m,i,j=-1,k,k
            while i<l:
                if m<=p[i]:
                    m=p[i]
                    j=i
                i+=1
            if p[j]==p[k]:
                k+=1
            else:
                p[j],p[k]=p[k],p[j]
                break
        return int(''.join([str(i) for i in p]))

print(Solution().maximumSwap(98368))
        
         
        