class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def help(m):          
            t = 0
            while m!=0:
                i = m%10
                t += i*i
                m//=10
            return t
        
        lst = []
        happy = False
        while True:
            t = help(n)
            if t==1 or t in lst:
                if t==1:
                    happy = True
                break
            if t!=0:
                lst.append(t)
                n=t
        print(lst)
        return happy


print(Solution().isHappy(5))


        
