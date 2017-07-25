class Codec:

    def __init__(self):
        self.db=dict()
        self.id=10000
        self.n=[chr(x) for x in range(65,91)]+[chr(x) for x in range(97,123)]+[chr(x) for x in range(48,58)]

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        self.db[self.id]=longUrl
        surl = 'http://tinyurl.com/'+self.__base__(self.id)
        self.id+=1
        return surl


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        t = shortUrl.split(r'/')[-1]
        return self.db[self.__decode__(t)]
    def __base__(self, num):
        r=''
        while num>0:
            r+=self.n[num%62]
            num//=62
        return r.ljust(6,'A')

    def __decode__(self,s):
        t=0
        for i,c in enumerate(s):
            t+=self.n.index(c)*pow(62,i)
        return t

# Your Codec object will be instantiated and called as such:
codec = Codec()
codec.decode(codec.encode('https://leetcode.com/problems/design-tinyurl'))