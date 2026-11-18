class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix = [0] * n
        suffix = [0] * n
        prefix[0] = nums[0]
        suffix[-1] = nums[-1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i]
        result[0] = suffix[1]
        result[-1] = prefix[-2]
        for i in range(1, n - 1):
            result[i] = prefix[i - 1] * suffix[i + 1]
        return result

        