class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        """
            initialize a set
            get three elements that sum to zero
            sort and store it in set

            [-1,0,1,2,-1,-4]
              - - -

        """
        # n = len(nums)
        # unique = set()
        # for i in range(n):
        #     for j in range(i+1, n):
        #         for k in range(j+1, n):
        #             current_sum = nums[i] + nums[j] + nums[k]
        #             if current_sum == 0:
        #                 current_ls = [nums[i], nums[j], nums[k]]
        #                 current_ls.sort()
        #                 unique.add(tuple(current_ls))
        
        # return [list(t) for t in unique]


        # n = len(nums)
        # unique = set(nums)
        # result_set = set()

        # for i in range(n):
        #     for j in range(i+1, n):
        #         diff = nums[i] + nums[j]
        #         if -diff in unique:
        #             current_ls = [nums[i], nums[j], -diff]
        #             current_ls.sort()
        #             result_set.add(tuple(current_ls))

        # return [list(t) for t in result_set]


        n = len(nums)
        nums.sort()
        print(nums)
        res = []
        start = 0

        while start < n:
            
            print(f"start: {start}")
            L = start + 1
            R = n - 1

            
            while L < R:

                sum = nums[L] + nums[R] + nums[start]
                
                if sum == 0:
                    print(f"start: {start} -- L : {L} -- R: {R}")
                    res.append([nums[start], nums[L], nums[R]])
                    L += 1
                    R -= 1
                    
                    while L < n-1 and nums[L] == nums[L - 1]: L += 1
                    while R > 0 and nums[R] == nums[R + 1]: R -= 1
                    
                elif sum > 0:
                    R -= 1
                    
                else:
                    L += 1

            start += 1
            while start < n - 1 and nums[start] == nums[start - 1]:
                start += 1

        return res       




