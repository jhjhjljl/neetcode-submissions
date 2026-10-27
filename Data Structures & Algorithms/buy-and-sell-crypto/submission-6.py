class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        length = len(prices)
        for i in range(length):
            for j in range(i + 1, length):
                current_profit = prices[j] - prices[i]
                max_profit = max(max_profit, current_profit)
        return max_profit