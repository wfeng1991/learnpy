class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        an=a.split(r'+')
        bn=b.split(r'+')
        a1,a2 = int(an[0]),int(an[1][:-1])
        b1,b2 = int(bn[0]),int(bn[1][:-1]) 
        _a=a1*b1-a2*b2
        _b=a1*b2+a2*b1
        return str(_a)+'+'+str(_b)+'i'

print(Solution().complexNumberMultiply("1+-1i", "0+0i"))