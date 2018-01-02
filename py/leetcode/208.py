class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data={}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        t=self.data
        for i,c in enumerate(word):
            if c not in t:
                t[c]={}
            if i==len(word)-1:
                t[c]['leaf']=None
            t=t[c]
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        t=self.data
        for c in word:
            if c in t:
                t=t[c]
            else:
                return False
        return 'leaf' in t

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        t=self.data
        for c in prefix:
            if c in t:
                t=t[c]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('abc')
obj.insert('ab')
print(obj.search('ab'))
print(obj.startsWith('ab'))