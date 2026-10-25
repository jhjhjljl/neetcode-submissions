class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zero_count = 0
        result = [0] * len(nums)
        for x in nums:
            if not x:
                zero_count += 1
            else:
                total_prod *= x
        if zero_count > 1:
            return result
        for i, x in enumerate(nums):
            if zero_count:
                result[i] = 0 if x else total_prod 
            else:
                result[i] = total_prod // x
        return result