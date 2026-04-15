class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        dp = {}

        def fn(i, curSum):
            
            if (i, curSum) in dp: 
                return dp[(i, curSum)]

            if i >= n or curSum > amount:
                return float("inf")
            
            if curSum == amount: 
                return 0

            pick = 1 + fn(i, curSum + coins[i])
            not_pick = fn(i+1, curSum)

            dp[(i, curSum)] = min(pick, not_pick)
            return dp[(i, curSum)]

        res = fn(0,0)

        return -1 if res == float("inf") else res



        