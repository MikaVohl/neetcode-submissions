class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy = [0 for _ in prices]
        for i, price in enumerate(prices):
            if i == 0:
                best_buy[i] = price
            else:
                best_buy[i] = min(best_buy[i-1], price)

        max_profit = 0
        for i, price in enumerate(prices):
            max_profit = max(max_profit, price - best_buy[i])

        return max_profit