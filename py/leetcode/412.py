class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        s3 = 'Fizz'
        s5 = 'Buzz'
        s15 = 'FizzBuzz'
        i = 1
        r = []
        while i <= n:
            if i%15==0:
                r.append(s15)
            elif i%3==0:
                r.append(s3)
            elif i%5==0:
                r.append(s5)
            else:
                r.append(str(i))
            i += 1
        return r

s =Solution()
print(s.fizzBuzz(15))
