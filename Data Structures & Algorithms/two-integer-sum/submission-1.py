"""
hm = {
    3: 0,
    5: 1,
    6: 2,
    4: 3
}

nums = [3, 5, 6, 4]
target = 7

[3, 5, 6, 4]
7 - 3 = 4 x
7 - 5 = 2 x
7 - 6 = 1 x
7 - 4 = 3  in the hm. o

time complexity: O(n)
space complexity: O(n)
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, x in enumerate(nums):
            diff = target - x
            if diff in num_to_index:
                return [num_to_index[diff], i]
            num_to_index[x] = i
        return []
        