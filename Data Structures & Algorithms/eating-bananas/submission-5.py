import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        result = 0
        while left <= right:
            k = (left + right) // 2
            current_hours = 0
            for x in piles:
                current_hours += math.ceil(x / k)
            if current_hours > h:
                left = k + 1
            else:
                result = k
                right = k - 1
        return result



        