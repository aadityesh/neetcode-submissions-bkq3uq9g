class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        dp = [-1] * n
        dp[-1] = True

        def dfs(i):

            if dp[i] != -1: return dp[i]
            if i >= n - 1: return True
            if nums[i] == 0: return False

            for jump in range(1, nums[i]+1):

                if (i + jump) >= n: break
                
                if dfs(i + jump):
                    dp[i] = True
                    return True

            dp[i] = False
            return False
        
        return dfs(0)

        # n = len(nums)
        
        # goal = n - 1 # index

        # for i in range(n - 1, -1, -1):
            
        #     if i + nums[i] >= goal:
        #         goal = i

        # return goal == 0



            
