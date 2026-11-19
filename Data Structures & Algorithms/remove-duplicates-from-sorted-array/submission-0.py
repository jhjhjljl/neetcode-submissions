"""
[1,1,2,3,4]
[1,2,2,3,4]
[1,2,3,3,4]
[1,2,3,4,4]
       l
         r 

left | right | array

"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        return left + 1


            
        