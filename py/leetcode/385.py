# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        self.i=0
        def nextItem(s):
            if self.i<len(s):
                if s[self.i].isdigit() or s[self.i]=='-':
                    buffer=''
                    while self.i<len(s) and (s[self.i].isdigit() or s[self.i]=='-'):
                        buffer+=s[self.i]
                        self.i+=1
                    return NestedInteger(int(buffer))
                if s[self.i]=='[':
                    ni=NestedInteger([])
                    self.i+=1
                    ni.getList().append(nextItem(s))
                    while s[self.i]==',':
                        self.i+=1
                        ni.getList().append(nextItem(s))
                    if s[self.i]==']':
                        self.i+=1
                        return ni
        return nextItem(s)

    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        self.i=0
        def nextItem(s):
            if self.i<len(s):
                if s[self.i].isdigit():
                    buffer=''
                    while self.i<len(s) and s[self.i].isdigit():
                        buffer+=s[self.i]
                        self.i+=1
                    return NestedInteger(int(buffer))
                if s[self.i]=='[':
                    ni=NestedInteger([])
                    self.i+=1
                    ni.add(nextItem(s))
                    if s[self.i]==',':
                        self.i+=1
                        ni.add(nextItem(s))
                    if s[self.i]==']':
                        self.i+=1
                        return ni
        return nextItem(s)

    def deserialize1(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        self.i=0
        def nextItem(s):
            if self.i<len(s):
                if s[self.i].isdigit() or s[self.i]=='-':
                    buffer=''
                    while self.i<len(s) and (s[self.i].isdigit() or s[self.i]=='-'):
                        buffer+=s[self.i]
                        self.i+=1
                    return int(buffer)
                if s[self.i]=='[':
                    ni=[]
                    self.i+=1
                    ni.append(nextItem(s))
                    while s[self.i]==',':
                        self.i+=1
                        ni.append(nextItem(s))
                    if s[self.i]==']':
                        self.i+=1
                        return ni
        return nextItem(s)


print(Solution().deserialize1('-3'))               

            
            
