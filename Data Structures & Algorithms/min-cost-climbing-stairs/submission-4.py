class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * (n + 1)
        # if n == 3: return min(nums[0], nums[1])

        # def solve(i):

        #     if i >= n:
        #         return 0

        #     if dp[i] != -1: return dp[i]

        #     oneStep = nums[i] + solve(i + 1)
        #     twoStep = nums[i] + solve(i + 2)

        #     dp[i] = min(oneStep, twoStep)
        #     return dp[i]
        
        # # return min(solve(0), solve(1))

        # dp[0], dp[1] = nums[0], nums[1]

        # for i in range(2, n):
        #     dp[i] = nums[i] + min(dp[i-1], dp[i-2])
        
        # return min(dp[n-1], dp[n-2])

        t0, t1 = nums[0], nums[1]
        for i in range(2, n):
            curr = min(t0, t1) + nums[i]
            t0 = t1
            t1 = curr
        
        return min(t0, t1)




        