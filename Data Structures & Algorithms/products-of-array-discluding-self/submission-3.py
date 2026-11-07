"""
[1, 2, 4, 6]

prefix
[1, 1, 1, 1]
[1, 1, 1, 1]
[1, 1, 2, 1]
[1, 1, 2, 8]

suffix
[1, 1, 1, 1]
[1, 1, 6, 1]
[1, 24, 6, 1]
[48, 24, 6, 1]
  


"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        for i in range(n):
            result[i] = prefix[i] * suffix[i]
        return result
        