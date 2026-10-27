class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        length = len(prices)
        for i in range(length):
            for j in range(i + 1, length):
                profit = prices[j] - prices[i]
                result = max(result, profit)
        return result
        