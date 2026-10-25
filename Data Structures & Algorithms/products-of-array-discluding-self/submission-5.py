class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        zero_count = 0
        zero_index = 0
        prod_total = 1
        result = [0] * length
        for i, x in enumerate(nums):
            if x:
                prod_total *= x
            else:
                zero_index = i
                zero_count += 1
        if zero_count > 1:
            return result
        elif zero_count == 1:
            result[zero_index] = prod_total
            return result
        else:
            for i in range(length):
                result[i] = prod_total // nums[i]
            return result

            
        
        
            