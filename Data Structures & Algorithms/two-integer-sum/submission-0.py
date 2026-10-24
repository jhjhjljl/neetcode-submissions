"""
my solution will use hashmap where the key will be the difference
required to get to target from ith element.
time complexity will be o(n).
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, x in enumerate(nums):
            if x in diff:
                return [diff[x], i]
            diff[target - x] = i
        return []
        