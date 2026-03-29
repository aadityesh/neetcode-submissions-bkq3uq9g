class Solution:
    def rob(self, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 1: return nums[0]

        dp = [-1] * (n)

        def solve(i, e):
            # print(f"i, e: {i, e}")
            if i > e:
                print(f"@ i, e: {i, e}")
                return 0

            if dp[i] != -1: return dp[i]

            steal = nums[i] + solve(i + 2, e)
            skip = solve(i + 1, e) 

            dp[i] = max(steal, skip)

            return dp[i]

        res1 = solve(0, n - 2)
        
        dp = [-1] * (n)
        res2 = solve(1, n - 1)

        return max(res1, res2)





        


