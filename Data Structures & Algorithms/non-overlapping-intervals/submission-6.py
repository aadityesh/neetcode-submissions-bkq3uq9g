class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        # n = len(intervals)
        # cnt = 0
        # intervals.sort()
        # res = [intervals[0]]

        # for i in range(1, n):

        #     if res[-1][1] > intervals[i][0]:
        #         res[-1][0], res[-1][1] = min(intervals[i][0], res[-1][0]), min(intervals[i][1], res[-1][1])
        #         cnt += 1
            
        #     else:
        #         res.append(intervals[i])

        # return cnt


        n = len(intervals)
        cnt = 0
        intervals.sort()

        end = intervals[0][1]

        for i in range(1, n):

            if end > intervals[i][0]:
                end = min(intervals[i][0], end)
                cnt += 1
            
            else:
                end = intervals[i][0]

        return cnt