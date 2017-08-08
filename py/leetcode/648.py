class Trie(object):
    def __init__(self,c,f):
        self.children=[None]*26
        self.c=c
        self.f=f

    def insert(self, w):
        if w:
            c=w[0]
            idx=ord(c)-ord('a')
            if self.children[idx] is None:
                self.children[idx]=Trie(c,len(w)==1)
            elif len(w)==1:
                self.children[idx].setf(True)
            self.children[idx].insert(w[1:])

    def setf(self,f):
        self.f= f

    def shortfind(self, w, l):
        if w:
            c=w[0]
            idx=ord(c)-ord('a')
            if self.children[idx] and self.children[idx].f:
                return l+1
            elif self.children[idx]:
                return self.children[idx].shortfind(w[1:],l+1)
            else:
                return 0
                
    
class Solution(object):
    def replaceWords(self, dic, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie=Trie(None,False)
        for w in dic:
            trie.insert(w)
        ws=sentence.split(' ')
        for i,w in enumerate(ws):
            n = trie.shortfind(w,0)
            if n:
                ws[i]=w[0:n]
        return ' '.join(ws)

print(Solution().replaceWords(["a", "aa", "aaa", "aaaa"],"a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa"))
