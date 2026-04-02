"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

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