class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, x in enumerate(nums):
            if x in diff:
                return [diff[x], i]
            diff[target - x] = i
        return []
        