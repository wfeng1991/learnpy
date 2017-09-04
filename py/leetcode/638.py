class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        def help(price, special, needs):
            res = sum([price[i]*needs[i] for i in range(len(price))])
            for s in special:
                tmpneeds=[i for i in needs]
                if res==0:
                    return 0
                t=0
                i=0
                l=len(s)-1
                while i<l:
                    if tmpneeds[i]-s[i]<0:
                        break
                    tmpneeds[i]-=s[i]
                    t+=s[i]*price[i]
                    i+=1
                if i==l:
                    t=min(t,s[l])
                    res=min(res,t+help(price, special, tmpneeds))
            return res
        return help(price, special, needs)

print(Solution().shoppingOffers([2,5],[[3,0,5],[1,2,10]],[3,2]))
                


