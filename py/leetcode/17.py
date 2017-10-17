class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic={
            '0':' ',
            '1':'',
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz',
        }
        res=[]
        def help(dic,digits,t,res,l):
            if t and len(t)==l:
                res.append(t)
            for i,d in enumerate(digits):
                for c in dic[d]:
                    help(dic,digits[i+1:],t+c,res,l)
        help(dic,digits,'',res,len(digits))
        return res

print(Solution().letterCombinations('234'))
            
