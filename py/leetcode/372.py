class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        # a^1234567 % k = (a^1234560 % k) * (a^7 % k) % k = (a^123456 % k)^10 % k * (a^7 % k) % k
        # Looks complicated? Let me put it other way:
        # Suppose f(a, b) calculates a^b % k; Then translate above formula to using f :
        # f(a,1234567) = f(a, 1234560) * f(a, 7) % k = f(f(a, 123456),10) * f(a,7)%k;
        a%=1337
        res=1
        i=0
        while b:
            res*=pow(pow(a,b.pop())%1337,pow(10,i))%1337
            res%=1337
            i+=1
        return res

print(Solution().superPow(2147483647,[2,0,0]))
