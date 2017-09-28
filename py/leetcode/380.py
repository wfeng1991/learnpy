from random import Random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic={}
        self.data=[]

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            return False
        else:
            self.data.append(val)
            self.dic[val]=len(self.data)-1
            return True        
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.dic:
            i = self.dic[val]
            if i<len(self.data)-1:
                self.data[i]=self.data[-1]
                self.dic[self.data[i]]=i
            self.data.pop()
            self.dic.pop(val,0)
            return True
        else:
            return False
        
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        
        return self.data[random.randint(0, len(self.data) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

randomSet =  RandomizedSet()

# Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(0)
randomSet.insert(1)

# Returns false as 2 does not exist in the set.
randomSet.remove(0)
randomSet.insert(2)
randomSet.remove(1)
randomSet.getRandom()