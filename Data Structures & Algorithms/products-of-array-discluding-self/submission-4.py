"""
[1, 2, 4, 6]

prefix = 1

store prefix at i
then multiply prefix with nums[i]

i = 0
[1, 1, 1, 1]
prefix = 1

i = 1
[1, 1, 1, 1]
prefix = 2

i = 2
[1, 1, 2, 1]
prefix = 8

i = 3
[1, 1, 2, 8]
prefix = 48

nums = [1, 2, 4, 6]
result = [1, 1, 2, 8]

suffix = 1

i = 3
[1, 1, 2, 8]
suffix = 6

i = 2
[1, 1, 12, 8]
suffix = 24

i = 1
[1, 24, 12, 8]
suffix = 48

i = 0
[48, 24, 12, 8]
suffix = 48

"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        prefix = 1
        suffix = 1
        for i in range(n):
            result[i] = prefix
            prefix = prefix * nums[i]
        for i in range(n - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * nums[i]
        return result
        