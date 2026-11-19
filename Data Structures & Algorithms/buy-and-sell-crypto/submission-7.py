"""
[10,3,5,1,7,1]
        l
          r

l | r | profit | max_profit
0 | 1 | -7     | 0
1 | 2 |  2     | 2
1 | 3 | -2     | 2
3 | 4 |  6     | 6

"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for right in range(1, len(prices)):
            current_profit = prices[right] - prices[left]
            max_profit = max(max_profit, current_profit)
            if prices[left] > prices[right]:
                left = right
        return max_profit
            

        