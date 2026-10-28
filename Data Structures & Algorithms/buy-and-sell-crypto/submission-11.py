class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l = 0
        r = 1
        result = 0
        while r < n:
            while prices[l] > prices[r]:
                l = r
            current_sum = prices[r] - prices[l]
            result = max(result, current_sum)
            r += 1
        return result