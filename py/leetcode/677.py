class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.dic[key]=val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        res=0
        for k in self.dic:
            if k.startswith(prefix):
                res+=self.dic[k]
        return res


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)