class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def help(s,index,t,subs,sl,res):
            if index==len(s):
                if sl==index:
                    res.append(subs)
                return
            p=t+s[index]
            if p==p[::-1]:
                help(s,index+1,'',subs+[p],sl+len(p),res)
            help(s,index+1,t+s[index],subs,sl,res)
        res=[]
        help(s,0,'',[],0,res)
        return res
print(Solution().partition('aab'))