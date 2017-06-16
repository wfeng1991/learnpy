class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return '0'
        d = {'0000':'0',
            '0001':'1',
            '0010':'2',
            '0011':'3',
            '0100':'4',
            '0101':'5',
            '0110':'6',
            '0111':'7',
            '1000':'8',
            '1001':'9',
            '1010':'a',
            '1011':'b',
            '1100':'c',
            '1101':'d',
            '1110':'e',
            '1111':'f'}
        i=0
        r=''
        m=1
        t=''
        while i<32:
            t=str((num>>i) & m)+t
            i+=1
            if i%4==0:
                r+=d[t]
                t=''
        r = r[::-1]
        n0=0
        for c in r:
            if c=='0':
                n0+=1
            else:
                break
        return r[n0:]

    def toHex1(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        HEX = '0123456789abcdef'
        cnt = 0
        output = ''
        while num != 0 and cnt < 8:
            output = HEX[num & 0xF] + output
            num = num >> 4
            cnt += 1
        return output
print(Solution().toHex(0))