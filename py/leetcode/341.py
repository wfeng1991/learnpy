# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
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

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def help(nlist,lst):
            for i in nlist:
                if i.isInteger():
                    lst.append(i.getInteger())
                else:
                    help(i.getList(),lst)
        self.idx=0
        self.lst=[]
        if len(nestedList)!=0:
            help(nestedList,self.lst)
        self.length=len(self.lst)
        
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            t = self.lst[self.idx]
            self.idx+=1
            return t
       
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.idx<self.length:
            return True
        else:
            return False


        

# Your NestedIterator object will be instantiated and called as such:
i, v = NestedIterator([[1,1],2,[1,1]]), []
while i.hasNext(): v.append(i.next())
print(v)
