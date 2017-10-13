class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic={}
        for s in strs:
            t=sorted(s)
            if t in dic:
                dic[t].append(s)
            else:
                dic[t]=[s]
        return [dic[x] for x in dic]