class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        dp = [-1] * (n)

        # def solve(i, e):
        #     # print(f"i, e: {i, e}")
        #     if i > e:
        #         print(f"@ i, e: {i, e}")
        #         return 0

        #     if dp[i] != -1: return dp[i]

        #     steal = nums[i] + solve(i + 2, e)
        #     skip = solve(i + 1, e) 

        #     dp[i] = max(steal, skip)

        #     return dp[i]

        # res1 = solve(0, n - 2)

        # dp = [-1] * (n)
        # res2 = solve(1, n - 1)

        # return max(res1, res2)

        # 0 ... N - 2

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        res1 = 0

        for i in range(2, n-1): # [2 ... n - 2]
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            res1 = max(res1, dp[i])
        

        dp = [-1] * (n) 
        dp[0], dp[1] = 0, nums[1]
        res2 = 0

        for i in range(2, n): # [2 ... n-1]
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            res2 = max(res2, dp[i])
        
        return max(res1, res2)
        

            



        


