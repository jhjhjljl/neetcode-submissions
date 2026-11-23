"""
[3,4,5,6,1,2]
         l
         r
       m
    

l | r | m
0 | 5 | 2  if nums[r] is less than nums[mid], move the left pointer
3 | 5 | 4  if nums[r] is greater or equal to nums[mid], move the right pointer
3 | 4 | 3  
"""



class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]
        