"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        n = len(intervals)
        if n == 0: return True
        intervals.sort(key=lambda x : x.start)
        res = [intervals[0]]
        
        for i in range(1, n):
            if res[-1].end > intervals[i].start:
                res[-1].start, res[-1].end = min(res[-1].start, intervals[i].start), max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        
        return res == intervals
            