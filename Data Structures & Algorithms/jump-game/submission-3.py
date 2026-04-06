class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [-1] * n

        def dfs(i):

            if i == n - 1: return True
            if nums[i] == 0: return False

            for jump in range(1, nums[i]+1):
                
                if dp[i + jump] != -1:
                    return dp[i + jump]
                
                elif dfs(i + jump):
                    dp[i + jump] = True
                    return dp[i + jump]


            dp[i] = False
            return dp[i]
        
        return dfs(0)
            
