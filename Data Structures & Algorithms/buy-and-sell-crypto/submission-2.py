class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)
        max_price, max_profit = 0, 0

        for i in range(n-1, -1, -1):
            current_profit = max_price - prices[i]
            max_price = max(max_price, prices[i])
            max_profit = max(max_profit, current_profit)

        return max_profit
        