class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dic = dict()
        for c in s:
            if c in dic:
                dic[c][1]+=1
            else:
                dic[c]=[c,1]
        v=dic.values()
        v=sorted(v,key=lambda x:-x[1])
        r=''
        for i in v:
            r+=i[0]*i[1]
        return r

Solution().frequencySort('aaabbccc')