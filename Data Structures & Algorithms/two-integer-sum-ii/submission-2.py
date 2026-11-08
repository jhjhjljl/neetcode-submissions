"""
[1, 2, 3, 4]
l   r

1 + 4 = 5 > 3
1 + 3 = 4 > 3
1 + 2 = 3 = 3 -> answer

time: O(n)
space: O(1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            current_sum = numbers[l] + numbers[r]
            if current_sum < target:
                l += 1
            elif current_sum > target:
                r -= 1
            else:
                return [l + 1, r + 1]
        return []
        