"""
k = 2
[1,4,3,2]
1 + 2 + 2 + 1 = 6 hours

k = 3
[1,4,3,2]
1 + 2 + 1 + 1 = 5 hours

k = 1
[1,4,3,2]
1 + 4 + 3 + 2 = 10 hours x

[1, 2, 3, 4]
    l  
    r

l | r | k | hrs
0 | 3 | 1 | 6 -> answer
0 | 1 | 0 | 10

"""
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        result = 0
        left = 1
        right = 0
        for x in piles:
            right = max(right, x)
        while left <= right:
            k = (left + right) // 2
            hours_taken = 0
            for x in piles:
                hours_taken += math.ceil(x / k)
            if hours_taken > h:
                left = k + 1 
            elif hours_taken <= h:
                result = k
                right = k - 1
        return result


        

        