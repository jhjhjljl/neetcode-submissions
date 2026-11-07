"""
[1, 2, 4, 6]
prefix
[1, 2, 8, 48]

postfix
[48, 48, 24, 6]
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0] * n
        postfix = [0] * n
        result = [0] * n
        prefix[0] = nums[0]
        postfix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]
        result[0] = postfix[1]
        result[-1] = prefix[-2]
        for i in range(1, n - 1):
            result[i] = prefix[i - 1] * postfix[i + 1]
        return result
            


        