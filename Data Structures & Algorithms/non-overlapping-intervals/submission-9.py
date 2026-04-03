class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        n = len(intervals)

        # sort to get earliest finished to last finished
        intervals.sort(key=lambda x: x[1]) 
        non_overlaps = 0 # cnt of non-overlapping
        lastEnd = float("-inf")

        for i in range(n):
            # start >= lastEnd
            if intervals[i][0] >= lastEnd:
                non_overlaps += 1
                lastEnd = intervals[i][1]
        
        return n - non_overlaps
