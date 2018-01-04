class Solution(object):
    def calculate1(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.isdigit():
            return int(s)
        self.p=0
        def nextToken(s):
            while self.p<len(s) and s[self.p]==' ':
                self.p+=1
            if self.p>=len(s):
                return
            if s[self.p].isdigit():
                num=''
                while self.p<len(s) and s[self.p].isdigit():
                    num+=s[self.p]
                    self.p+=1
                return int(num)
            else:
                op=s[self.p]
                self.p+=1
                return op
        nums=[]
        ops=[]
        while True:
            t=nextToken(s)
            if t is not None:
                if isinstance(t,int):
                    nums.append(t)
                else:
                    if t=='*':
                        nums[-1]*=nextToken(s)
                    elif t=='/': 
                        nums[-1]//=nextToken(s)
                    else:
                        ops.append(t)
            else:
                break
        while ops:
            t=ops.pop(0)
            if t=='+':
                n1=nums.pop(0)
                n2=nums.pop(0)
                nums.insert(0,n1+n2)
            elif t=='-':
                n1=nums.pop(0)
                n2=nums.pop(0)
                nums.insert(0,n1-n2)
        return nums[0]

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s.isdigit():
            return int(s)
        self.p=0
        def nextToken(s):
            while self.p<len(s) and s[self.p]==' ':
                self.p+=1
            if self.p>=len(s):
                return
            if s[self.p].isdigit():
                num=''
                while self.p<len(s) and s[self.p].isdigit():
                    num+=s[self.p]
                    self.p+=1
                return int(num)
            else:
                op=s[self.p]
                self.p+=1
                return op
        nums=[]
        while True:
            t=nextToken(s)
            if t is not None:
                if t=='*':
                    nums[-1]*=nextToken(s)
                elif t=='/': 
                    nums[-1]=int(nums[-1]/nextToken(s))
                elif t=='-':
                    nums.append(-nextToken(s))
                elif t=='+':
                    nums.append(nextToken(s))
                else:
                    nums.append(t)
            else:
                break
        return sum(nums)
        

print(Solution().calculate("14-3/2"))
            