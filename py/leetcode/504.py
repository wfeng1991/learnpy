class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        if num<0:
            return '-'+self.convertToBase7(-num)
        r=''
        i=1
        while num>0:
            t = num%pow(7,i)//pow(7,i-1)
            num-=t*pow(7,i-1)
            r+=str(t)
            i+=1
        return r[::-1]

print(Solution().convertToBase7(56))