"""
[1,7,2,5,4,7,3,6]
   l             
             r


left | right | area
0    | 7     | 7
1    | 7     | 36 
1    | 6     | 15 

"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            current_area = width * height
            max_area = max(max_area, current_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area
        