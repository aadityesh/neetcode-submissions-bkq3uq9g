class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1. Append the newInterval in the list.
        2. sort it again
        3. MergeInterval Logic


        
        """

        intervals.append(newInterval)
        intervals.sort()

        n = len(intervals)
        res = [intervals[0]] 

        for i in range(1, n):
            
            # [1, 3] >= [2, 5]
            if res[-1][1] >= intervals[i][0]:
                res[-1][0], res[-1][1] = min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])

        
        return res
                
