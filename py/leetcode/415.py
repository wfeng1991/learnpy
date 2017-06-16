class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)
        l2 = len(num2)
        if l1 > l2:
            return self.addStrings(num2, num1)
        i = 0
        r = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        while i<l2:
            if i<l1:
                r += (ord(num1[i])+ord(num2[i])-48*2)*pow(10,i)
            else:
                r += (ord(num2[i])-48)*pow(10,i)
            i+=1
        return str(r)

print(Solution().addStrings('98','9'))
        