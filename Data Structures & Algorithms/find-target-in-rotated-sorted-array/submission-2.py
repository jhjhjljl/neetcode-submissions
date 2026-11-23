"""
target = 4
[6,1,2,3,4,5]
       l
           r
         m
l | r | m
0 | 5 | 2
3 | 5 | 4

"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[right] >= target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1



            
        