"""
[10,1,5,6,7,1]
    i     j


i | j | current_profit | max_profit
0 | 1 | -9             | 0
0 | 2 | -5             | 0
0 | 3 | -4             | 0
...
1 | 2 | 4              | 4
1 | 3 | 5              | 5
1 | 4 | 6              | 6
...

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
