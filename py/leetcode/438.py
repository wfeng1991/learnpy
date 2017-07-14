class Solution(object):
    #遍历 暴力解法
    def findAnagrams1(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls= len(s)
        lp= len(p)
        if ls<lp or lp==0:
            return []
        dic = dict()
        for c in p:
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        import copy
        r=[]
        for i in range(0,ls-lp+1):
            t = copy.deepcopy(dic)
            f = True
            for j in range(i,i+lp):
                if s[j] in t and t[s[j]]>0:
                    t[s[j]]-=1
                else:
                    f=False
                    break
            if f:
                r.append(i)
        return r
    
    # 滑动窗口
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ls= len(s)
        lp= len(p)
        if ls<lp or lp==0:
            return []
        dic = dict()
        for c in p:
            if c in dic:
                dic[c]+=1
            else:
                dic[c]=1
        left,right=0,0
        r=[]
        count=lp
        while right<ls:
            if s[right] in dic:
                dic[s[right]]-=1
                if dic[s[right]]>=0:
                    count-=1
            
            right+=1
            
            if count==0:
                r.append(left)
            
            if right-left==lp:
                if s[left] in dic:
                    dic[s[left]]+=1
                    if dic[s[left]]>0:
                        count+=1
                left+=1
        return r
                

            


print(Solution().findAnagrams('abab','ab'))


        
        