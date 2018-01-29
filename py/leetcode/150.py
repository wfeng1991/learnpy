class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nums=[]
        while tokens:
            op = tokens.pop(0)
            if op=='+':
                n1=nums.pop()
                n2=nums.pop()
                nums.append(n2+n1)
            elif op=='-':
                n1=nums.pop()
                n2=nums.pop()
                nums.append(n2-n1)
            elif op=='*':
                n1=nums.pop()
                n2=nums.pop()
                nums.append(n2*n1)
            elif op=='/':
                n1=nums.pop()
                n2=nums.pop()
                nums.append(int(n2/n1))
            else:
                nums.append(int(op))
        return nums[0]
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

# print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))


