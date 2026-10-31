"""
prices = [10,1,5,6,7,1]
output = 6 

10,2,5,6,1,3
l  r          -8
   l r         3
   l   r       4
   l     r    -1
         l  r  2
max_profit = 4
time complexity: O(n)
space complexity: O(1)
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        l = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                max_profit = max(max_profit, prices[r] - prices[l])
        return max_profit
        
        

            
        