# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals)<=1:
            return intervals
        intervals = sorted(intervals,key=lambda i:i.start)
        intervals += [Interval(1000000,2000000)]#哨兵 典型值
        res=[]
        current,nextp=intervals[0],1
        while nextp<len(intervals):
            if current.start<=intervals[nextp].start and current.end>=intervals[nextp].end:
                nextp+=1
                continue
            elif current.end>=intervals[nextp].start and current.end<=intervals[nextp].end:
                current=Interval(current.start,intervals[nextp].end)
            else:
                res.append(current)
                current=intervals[nextp]
            nextp+=1
        return res
        
