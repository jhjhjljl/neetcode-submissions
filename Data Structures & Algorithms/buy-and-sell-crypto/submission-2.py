class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left_ptr = 0
        right_ptr = 1
        result = 0
        while right_ptr < len(prices):
            if prices[right_ptr] > prices[left_ptr]: 
                profit = prices[right_ptr] - prices[left_ptr]
                result = max(result, profit)
            else:
                left_ptr = right_ptr
            right_ptr += 1
        return result