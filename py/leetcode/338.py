class Solution(object):
    def countBits1(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r=[]
        cnt=0
        for n in range(0,num+1):
            i=0
            while i<32:
                cnt+=n&1
                n>>=1
                i+=1
            r.append(cnt)
            cnt=0
        return r
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        r = [0]*(num+1)
        i=1
        while i<=num:
            r[i]=r[i>>1]+(i&1)
            i+=1
        return r
print(Solution().countBits(5))