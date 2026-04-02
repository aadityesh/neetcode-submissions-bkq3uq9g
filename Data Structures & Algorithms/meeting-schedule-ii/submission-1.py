"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def printInterval(self, res):
        for i in res:
            print(i.start, i.end)

    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        
        n = len(intervals)

        if n <= 1: return n

        cnt = 1
        intervals.sort(key=lambda x: x.end)

        prevEnd = intervals[0].end

        for i in range(1, n):

            if prevEnd < intervals[i].start:
                continue
            else:
                cnt += 1
                prevEnd = intervals[i].end

        
        return cnt


            

        