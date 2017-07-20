class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data=[]
        self.mins=[]
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if len(self.mins)==0 or self.mins[-1] >= x:
            self.mins.append(x)
        elif self.mins[-1] < x:
            self.mins.append(self.mins[-1])
        self.data.append(x)
        

    def pop(self):
        """
        :rtype: void
        """
        self.data.pop()
        self.mins.pop()
        

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()