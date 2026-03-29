class Solution:
    def minCostClimbingStairs(self, nums: List[int]) -> int:

        n = len(nums)
        dp = [-1] * n
        # if n == 3: return min(nums[0], nums[1])

        def solve(i):

            if i >= n:
                return 0

            if dp[i] != -1: return dp[i]

            oneStep = nums[i] + solve(i + 1)
            twoStep = nums[i] + solve(i + 2)

            dp[i] = min(oneStep, twoStep)
            return dp[i]
        
        return min(solve(0), solve(1))
        