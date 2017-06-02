class Solution(object):
    def romanToInt(self, num):
        """
        :type num: str
        :rtype: int
        """
        tagVal={}
        tagVal['I'] = 1  
        tagVal['V'] = 5  
        tagVal['X'] = 10  
        tagVal['C'] = 100  
        tagVal['M'] = 1000  
        tagVal['L'] = 50  
        tagVal['D'] = 500
        l = len(num)
        r = 0
        for i,c in enumerate(num):
            t = i+1
            if t<l and tagVal[c]<tagVal[num[t]]:
                r-=tagVal[c]
            else:
                r+=tagVal[c]
        return r



print(Solution().romanToInt("DCXXI"))