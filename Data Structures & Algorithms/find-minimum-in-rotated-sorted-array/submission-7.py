"""
[3,4,5,6,1,2]
         l
         r
       m

    
l | r | m 
0 | 5 | 2
3 | 5 | 4
3 | 4 | 3
4 | 4 | 4
"""



class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[right] < nums[mid]:
                left = mid + 1
            elif nums[right] >= nums[mid]:
                right = mid
        return nums[left]
        
        

        