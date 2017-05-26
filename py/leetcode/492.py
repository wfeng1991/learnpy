class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]  l>=w
        """
        import math
        a = int(math.sqrt(area))
        r = [area, 1]
        while area%a != 0:
            a = a-1
        r[0]=area//a
        r[1]=a
        return r

        # import math
        # root = math.sqrt(area)
        # a=area
        # b=1
        # r = [a, b]
        # for i in range(1,area//2+1):
        #     if area//i * i==area and i<=root:
        #         a=i
        #         b=area//i
        #     elif i<=root:
        #         continue
        #     else:
        #         break
        # if a<=b:
        #     r=[b,a]
        # return r

    

print(Solution().constructRectangle(1222221))