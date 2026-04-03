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

            The Line Sweep :

            Think of each meeting as two events on a timeline:
            A start → someone walks into a meeting room (+1)
            An end → someone walks out of a room (-1)

            If you sort all these events by time and sweep through them, 
            you're essentially simulating a running count of occupied rooms. 
            The maximum that counter ever reaches is your answer.


            ----------

            Say this:

            “I convert each meeting into two events — a start and an end. 
            Then I sort all events by time, ensuring that end events are processed 
            before start events if they occur at the same time. As I sweep 
            through the timeline, I track how many meetings are active. 
            The maximum number of active meetings at any point gives 
            the minimum number of rooms required.”


            [(0,40),(5,10),(15,20)]
            [
                0, 1
                5, 1
                10, -1
                15, 1
                20, -1
                40, -1

            ]

        """

        events = []
        for interval in intervals:
            events.append((interval.start, 1))
            events.append((interval.end, -1))

        events.sort()

        cnt = 0
        maxCnt = 0

        for interval, status in events:
            cnt += status
            maxCnt = max(cnt, maxCnt)

        return maxCnt
            

