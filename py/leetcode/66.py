class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = True
        for n in digits:
            if n!=9:
                carry=False
                break
        l=len(digits)
        if carry:
            return [1]+list([0 for i in range(0, l)])
        i=l-1
        car=1
        while i>=0:
            digits[i]+=car
            if digits[i]==10:
                digits[i]=0
                car=1
            else:
                car=0
            i-=1
        return digits

print(Solution().plusOne([9]))