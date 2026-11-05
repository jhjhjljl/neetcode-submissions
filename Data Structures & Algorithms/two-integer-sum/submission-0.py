"""
[3, 4, 5, 6]

3 + 4 = 7 o
3 + 5 = 8 x
3 + 6 = 9 x

4 + 5 = 9 x
4 + 6 = 10 x

5 + 6 = 11 x
time complexity: O(n^2)
space complexity: O(1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        