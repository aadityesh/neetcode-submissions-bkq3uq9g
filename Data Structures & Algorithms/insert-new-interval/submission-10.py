class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        1. Append the newInterval in the list. 
        2. sort it again
        3. MergeInterval Logic


        
        """

        # intervals.append(newInterval)
        # intervals.sort()

        # n = len(intervals)
        # res = [intervals[0]] 

        # for i in range(1, n):
            
        #     # [1, 3] >= [2, 5]
        #     if res[-1][1] >= intervals[i][0]:
        #         res[-1][0], res[-1][1] = min(res[-1][0], intervals[i][0]), max(res[-1][1], intervals[i][1])
        #     else:
        #         res.append(intervals[i])

        
        # return res


        n = len(intervals)
        res = []
        i = 0

        # Non Overlapping on left side
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        print(f"@ {i}")


        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0], newInterval[1] = min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])
            i += 1
        
        res.append(newInterval)

        # Non Overlapping on right side

        while i < n and intervals[i][0] > newInterval[1]:
            res.append(intervals[i])
            i += 1

        
        return res

        # [6, 7] - [9, 10]
                
