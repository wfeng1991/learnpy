class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        l=len(data)
        i=0
        while i<l:
            m=0b10000000
            d=data[i]
            ul=0
            while d&m==m:
                ul+=1
                d<<=1
            if ul==0:
                i+=1
                continue
            elif ul==1 or ul>4:
                return False
            while ul>1 and i<l:
                i+=1
                ul-=1
                if i<l and data[i]>>7 == 1 and data[i]>>6 == 2:
                    pass
                else:
                    return False
            i+=1
        if i==l:
            return True
        else:
            return False

