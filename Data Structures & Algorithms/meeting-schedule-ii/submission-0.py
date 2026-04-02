"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        
        n = len(intervals)

        if n <= 1: return n

        cnt = 0
        intervals.sort(key=lambda x: x.start)
        res = [intervals[0]]

        for i in range(1, n):

            if res[-1].end > intervals[i].start:
                res[-1].start, res[-1].end = min(intervals[i].start, res[-1].start), max(intervals[i].end, res[-1].end)
                cnt += 1
            
            else:
                res.append(intervals[i])

        return cnt
        