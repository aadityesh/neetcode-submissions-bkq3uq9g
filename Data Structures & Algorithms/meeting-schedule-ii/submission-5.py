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

        cnt = 0
        maxCnt = 1
        intervals.sort(key=lambda x: x.start)

        prevEnd = intervals[0].end

        for i in range(1, n):
            
            # merge
            if prevEnd > intervals[i].start:
                prevEnd = max(prevEnd, intervals[i].end)
                cnt += 1
            else:
                cnt = 0

            maxCnt = max(maxCnt, cnt)

        self.printInterval(intervals)
        return maxCnt


            

        