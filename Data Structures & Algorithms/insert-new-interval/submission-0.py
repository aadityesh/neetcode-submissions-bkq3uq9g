class Solution:
    def insert(self, nums: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        
        
        """
            nums = [[1,3],[4,6]]
            newInterval = [2, 5]

            Sol:

                res = [[1, 3]]

                1. Merge newInterval:
                        - if a < b and not inserted - push
                2. Merge Current
                3. else not overlapping then simply dump them

        """
        
        n = len(nums)
        inserted = False
        res = [nums[0]]

        for i in range(1, n):

            # merge new interval
            if not inserted and res[-1][1] >= newInterval[0]:
                res[-1][0], res[-1][1] = min(res[-1][0], newInterval[0]), max(res[-1][1], newInterval[1])
                inserted = True
            
            # merge current
            if res[-1][1] >= nums[i][0]:
                res[-1][0], res[-1][1] = min(res[-1][0], nums[i][0]), max(res[-1][1], nums[i][1])


            # no merge found
            elif not inserted and newInterval[1] < nums[i][0]:
                res.append(newInterval)
                res.append(nums[i])
                inserted = True
            
            else:
                res.append(nums[i])

        return res


            

        
        






        