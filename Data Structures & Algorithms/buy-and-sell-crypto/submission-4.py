"""
[10,1,5,6,7,1]
    l       r

buy | sell | max_profit
10  | 1    | 0
1   | 5    | 4
1   | 6    | 5
1   | 7    | 6
1   | 1    | 6

move left pointer to right if prices[l] is greater than prices[r]
else we increment r until it's exhausted.

time: O(n)
space: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        r = 1
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
            r += 1
        return max_profit
        