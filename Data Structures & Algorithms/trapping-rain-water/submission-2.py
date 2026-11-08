"""
max_left = 4
max_right = 5
[4,2,0,3,2,5]
   l
           r

height | area | 
4      |  0   |  
2      |  2   |   

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = height[0]
        max_right = height[-1]
        l = 0
        r = len(height) - 1
        result = 0
        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                result += (max_left - height[l])
                l += 1
            else:
                max_right = max(max_right, height[r])
                result += (max_right - height[r])
                r -= 1
        return result
        