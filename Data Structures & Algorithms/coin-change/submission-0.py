class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)

        def fn(i, curSum):

            if i >= n or curSum > amount:
                return float("inf")
            
            if curSum == amount: 
                return 0

            pick = 1 + fn(i, curSum + coins[i])
            not_pick = fn(i+1, curSum)

            return min(pick, not_pick)

        res = fn(0,0)

        return -1 if res == float("inf") else res



        