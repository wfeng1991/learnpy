# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):

    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        lst = [[x,i] for i,x in enumerate(intervals)]
        lst = sorted(lst, key=lambda x: x[0].start)
        l=len(lst)
        i=0
        r=[-1]*l
        while i<l:
            d=lst[i][0]
            j=-1
            p=i+1
            while p<l:
                if d.end<=lst[p][0].start:
                    j=lst[p][1]
                    break
                p+=1
            r[lst[i][1]]=j
            i+=1
        return r

l=[[1,4],[2,3],[3,4]]
ins = [Interval(x[0],x[1]) for x in l]

print(Solution().findRightInterval(ins))

