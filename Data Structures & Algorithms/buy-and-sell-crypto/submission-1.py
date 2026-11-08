"""
max_profit = 0
[10,1,5,6,7,1]


l  | r | max_profit
10 | 1 | 0
1  | 5 | 4
1  | 6 | 5
1  | 7 | 6
1  | 1 | 6 
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        return max_profit
        