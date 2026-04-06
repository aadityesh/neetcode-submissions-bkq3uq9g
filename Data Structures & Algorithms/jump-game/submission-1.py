class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [-1] * n

        def dfs(i):

            if i == n - 1: return True
            if nums[i] == 0: return False
            if dp[i] != -1: return dp[i]
            
            for jump in range(1, nums[i]+1):
                if dfs(i + jump):
                    dp[i] = True
                    return dp[i]

            dp[i] = False
            return dp[i]
        
        return dfs(0)
            
