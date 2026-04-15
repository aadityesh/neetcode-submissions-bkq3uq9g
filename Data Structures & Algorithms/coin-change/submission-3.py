class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = {}
        def fn(remaining):
            
            if remaining in dp: 
                return dp[remaining]

            if remaining == 0: 
                return 0
    
            res = float("inf")
            for coin in coins:
                if remaining - coin >= 0:
                    res = min(res, 1 + fn(remaining - coin))

            dp[remaining] = res
            return dp[remaining]
        
        res = fn(amount)
        return -1 if res == float("inf") else res