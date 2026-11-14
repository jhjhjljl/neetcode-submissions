"""
[1,1,0,1,1,1]
       i

i | current_streak | max_streak
0 | 1              | 0
1 | 2              | 0
3 | 0              | 2
4 | 1              | 2
5 | 2              | 2
6 | 3              | 2
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak = 0
        max_streak = 0
        for x in nums:
            if x == 1:
                current_streak += 1
            else:
                max_streak = max(max_streak, current_streak)
                current_streak = 0
        return max(max_streak, current_streak)

        
        