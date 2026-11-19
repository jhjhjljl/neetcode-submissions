"""
[2,1,5,1,5,3]
 l
   r

l | r | current_sum | window_size | result 
0 | 0 | 2           | 1           | 0
0 | 1 | 3           | 2           | 0
0 | 2 | 8           | 3           | 0
0 | 3 | 9           | 4           | 0
0 | 4 | 14          | 5           | 5 
1 | 4 | 12          | 4           | 4 
2 | 4 | 11          | 3           | 3 
3 | 4 | 6           | 2           | 3 
3 | 5 | 9           | 3           | 3 
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        left = 0
        current_sum = nums[left]
        if current_sum >= target:
            return 1
        for right in range(1, len(nums)):
            current_sum += nums[right]
            while current_sum >= target:
                result = min(result, right - left + 1)
                current_sum -= nums[left]
                left += 1
        if result == float("inf"):
            return 0
        else:
            return result
        
            
            

        