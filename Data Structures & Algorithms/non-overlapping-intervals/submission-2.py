class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)
        intervals.sort()
        res = [intervals[0]]
        cnt = 0

        for i in range(1, n):
            if res[-1][1] > intervals[i][0]:
                # res[-1][0], res[-1][1] = min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])
                cnt+=1
            else:
                res.append(intervals[i])
        
        return cnt
            