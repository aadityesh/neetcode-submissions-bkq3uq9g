class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [0] * (n)

        # def solve(i):

        #     if i >= n: return 0

        #     if dp[i] != -1:
        #         return dp[i]

        #     steal = nums[i] + solve(i + 2)
        #     skip = solve(i + 1)

        #     dp[i] = max(steal, skip)

        #     return dp[i]
        
        # return solve(0)

        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        
        print(dp)
        return dp[-1]

        
            