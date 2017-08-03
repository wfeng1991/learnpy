class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        dic = dict()
        for s in paths:
            v = s.split(' ')
            pre=v[0]
            i=1
            while i<len(v):
                vv = v[i].split('(')
                # dic[pre+'/'+vv[0]]=vv[1][:-1]
                t=vv[1][:-1]
                if t in dic:
                    dic[t].append(pre+'/'+vv[0])
                else:
                    dic[t]=[pre+'/'+vv[0]]
                i+=1
        r=[dic[x] for x in dic if len(dic[x])>1]
        return r

print(Solution().findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)", "root/c 3.txt(abcd)", "root/c/d 4.txt(efgh)", "root 4.txt(efgh)"]))
