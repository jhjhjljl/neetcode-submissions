"""
try every combination

time: O(n^2)
space: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        for i in range(n):
            for j in range(i + 1, n):
                max_profit = max(max_profit, prices[j] - prices[i])
        return max_profit
        