class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        operators={'+':lambda a,b:a+b,
                   '-':lambda a,b:a-b,
                   '*':lambda a,b:a*b}
        nums=[]
        for i,c in enumerate(input):
            if c in operators:
                nl=self.diffWaysToCompute(input[:i])
                nr=self.diffWaysToCompute(input[i+1:])
                for n1 in nl:
                    for n2 in nr:
                        t=operators[c](n1,n2)
                        nums.append(t)
        if not nums:
            nums.append(int(input))
        return nums
        
print(Solution().diffWaysToCompute('2*3-4*5'))                    
                    
            
                
                
