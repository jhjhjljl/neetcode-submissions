"""
brute force solution.
time complexity: o(n^2)
space complexity: o(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i + 1, n):
                current_profit = prices[j] - prices[i]
                max_profit = max(max_profit, current_profit)
        return max_profit
        