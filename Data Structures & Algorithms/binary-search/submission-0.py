"""
[-1,0,2,4,6,8]
        l    
        m
        r

l | r | m
0 | 5 | 2
3 | 5 | 4
3 | 3 | 
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                return mid
        return -1
        