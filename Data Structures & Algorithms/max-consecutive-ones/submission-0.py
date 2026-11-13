"""
find maximum streak when 1 is shown in the array.

[1,1,0,1,1,1]
         i

i | current_streak | max_streak
0 | 1              | 1
2 | 2              | 2
3 | 0              | 2
4 | 1              | 2
5 | 2              | 2
6 | 3              | 3
"""
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_streak = 0
        current_streak = 0
        for x in nums:
            if x == 1:
                current_streak += 1
            else:
                current_streak = 0
            max_streak = max(max_streak, current_streak)
        return max_streak
            
        