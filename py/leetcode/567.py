class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # s1 in s2
        dic={}
        for c in s1:
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        l=len(s1)
        start,end=0,0
        count=0
        while start<len(s2):
            while end<len(s2) and end-start+1<=l:
                if s2[end] in dic:
                    if dic[s2[end]]>0:
                        count+=1
                    dic[s2[end]]-=1
                end+=1
            if count==l:
                return True
            if s2[start] in dic:
                if dic[s2[start]]>=0:
                    count-=1
                dic[s2[start]]+=1
            start+=1
        return False

print(Solution().checkInclusion("hello","ooolleoooleh"))

            
