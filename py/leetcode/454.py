class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = dict()
        for i in A:
            for j in B:
                s=i+j
                if s in dic:
                    dic[s]+=1
                else:
                    dic[s]=1
        res=0
        for i in C:
            for j in D:
                s=-1*(i+j)
                if s in dic:
                    res+=dic[s]
        return res