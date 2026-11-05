"""
[1, 2, 3, 4]
[1, 2]
    [2, 3]
        [3, 4]

[1, 2, 3, 3]
[1, 2]
    [2, 3]
       [3, 3]
time complexity: O(nlogn) 
space complextiy: O(n)
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
        
        