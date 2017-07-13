class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        pre='1'
        cur=''
        cnt=0
        num=''
        for i in range(2,n+1):
            for j in range(0,len(pre)):
                if num=='' or num==pre[j]:
                    cnt+=1
                    num=pre[j]
                if num!=pre[j]:
                    cur+=str(cnt)+num
                    cnt=1
                    num=pre[j]
                if j==len(pre)-1:
                    cur+=str(cnt)+num
            pre = cur
            cur = ''
            cnt=0
            num=''
        return pre

print(Solution().countAndSay(5))

                

        
