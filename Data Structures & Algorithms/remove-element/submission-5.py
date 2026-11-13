"""
nums = [0,1,2,2,3,0,4,2], val = 2

[0,1,2,2,3,0,4,2]
               i 
           k
i | k | nums
0 | 0 | [0,1,2,2,3,0,4,2] 
1 | 1 | [0,1,2,2,3,0,4,2]
2 | 2 | [0,1,2,2,3,0,4,2]
3 | 2 | [0,1,2,2,3,0,4,2] 
4 | 2 | [0,1,3,2,3,0,4,2] 
5 | 3 | [0,1,3,0,3,0,4,2] 
6 | 4 | [0,1,3,0,4,0,4,2] 
7 | 5 | [0,1,3,0,4,0,4,2] -> done 

time: O(n)
space: O(1)
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
            
        