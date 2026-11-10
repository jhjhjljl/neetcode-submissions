"""
[10,1,5,6,7,1]
    l
            r

l | r | current_profit | max_profit
0 | 1 | -9             | 0 
1 | 2 | 4              | 4
1 | 3 | 5              | 5
1 | 4 | 6              | 6
1 | 5 | 0              | 0
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            max_profit = max(max_profit, prices[r] - prices[l])
            print(max_profit)
            r += 1
        return max_profit
            
        