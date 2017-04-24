class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        r = ''
        base1 = {1:'I', 2:'II', 3:'III', 4:'IV', 5:'V', 6:'VI', 7:'VII', 8:'VIII', 9:'IX'}
        base10 = {10:'X', 20:'XX', 30:'XXX', 40:'XL', 50:'L', 60:'LX', 70:'LXX', 80:'LXXX', 90:'XC'}
        base100 = {100:'C', 200:'CC', 300:'CCC', 400:'CD', 500:'D', 600:'DC', 700:'DCC', 800:'DCCC', 900:'CM'}
        base1000 = {1000:'M', 2000:'MM', 3000:'MMM'}
        base = {0:base1,1:base10,2:base100,3:base1000}
        i = 0
        while num > 0:
            low = num % 10 * pow(10, i)
            num = num // 10
            if low != 0:
                r += base[i][low][::-1]
            i = i+1
            
        return r[::-1]

s = Solution()
print(s.intToRoman(3999))