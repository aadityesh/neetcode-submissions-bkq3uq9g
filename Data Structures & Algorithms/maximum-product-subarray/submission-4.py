class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [ ([-1] * n) for _ in range(n)]

        def calcMaxProduct(i, j):
            if i > j:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = nums[i] * calcMaxProduct(i+1, j)
            return dp[i][j]

        maxProd = float("-inf")
        for i in range(n):
            for j in range(i, n):
                maxProd = max(maxProd, calcMaxProduct(i, j))
        
        return maxProd