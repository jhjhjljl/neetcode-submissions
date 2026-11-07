"""
nums = [1, 2, 4, 6]

result = [1, 1, 1, 1]

[1, 1, 1, 1] i = 0, left_product = 1
[1, 1, 1, 1] i = 1, left_product = 2
[1, 1, 2, 1] i = 2, left_product = 8
[1, 1, 2, 8] i = 3, left_product = 48

[1, 1, 2, 8] i = 3, right_product = 6
[1, 1, 12, 8] i = 2, right_product = 24 
[1, 24, 12, 8] i = 1, right_product = 48 
[48, 24, 12, 8] i = 0, right_product = 48 

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




        
        