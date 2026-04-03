"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

# [1, 3], [2, 4] -> [1, 4]
# [1, 3], [2, 4] -> [1, 3]

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
            The Core Insight:
            At any point in time, 
            the number of rooms needed = number of meetings happening simultaneously. 
            You want the max or peak of that count.
        """
        map = defaultdict(int)
        for obj in intervals:
            map[obj.start] += 1
            map[obj.end] += -1
        
        cnt = 0
        maxCnt = 0
        
        for i in sorted(map.keys()):
            cnt += map[i]
            maxCnt = max(maxCnt, cnt)
        
        return maxCnt