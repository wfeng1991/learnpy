class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        la=len(a)
        lb=len(b)
        if la<lb:
            return self.addBinary(b,a)
        a=a[::-1]
        b=b[::-1]
        i = 0
        carry=0
        r=''
        while i<la:
            ia=ord(a[i])-48
            ib=0
            if i<lb:
                ib=ord(b[i])-48
            if ia+ib+carry==3:
                r='1'+r
                carry=1
            elif ia+ib+carry==2:
                r='0'+r
                carry=1
            else:
                r=str(ia+ib+carry)+r
                carry=0
            i+=1
        if carry==1:
            r='1'+r
        return r

print(Solution().addBinary('1010','1011'))
            
            