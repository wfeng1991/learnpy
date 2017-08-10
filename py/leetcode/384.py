class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.o=nums
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.o

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        r=[]
        l=len(self.o)
        import random
        t=[x for x in self.o]
        while len(r)<l:
            i=random.randint(0,len(t)-1)
            r.append(t[i])
            t=t[:i]+t[i+1:]
        return r
        


        


# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
param_1 = obj.reset()
param_2 = obj.shuffle()
print(param_2)