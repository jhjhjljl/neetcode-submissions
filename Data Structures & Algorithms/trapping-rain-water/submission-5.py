"""
we can solve this with two pointers, one starting at the left edge and one at the right edge, moving them inward toward each other. 

the key idea is that the amount of water that can be trapped at any position is limited by the shorter of the maximum heights found so far on its left and its right. 

so, we keep track of max_left and max_right as we go. at each step, we look at the two pointers, pick the side with the smaller height, and move that pointer inward. because the water level is bounded by the shorter side, we know for sure how much water can be trapped at that position. we calculate the water by subtracting the current height from our max height on that side, add it to our total, and repeat until the two pointers meet.

[0,2,0,3,1,0,1,3,2,1]
       l                
         r

l | r | max_left | max_right | area
0 | 1 | 0        | 0         | 0
2 | 1 | 2        | 0         | 0
2 | 2 | 2        | 2         | 0
2 | 3 | 2        | 3         | 0
0 | 3 | 2        | 3         | 2
3 | 3 | 3        | 3         | 0
3 | 1 | 3        | 3         | 2
3 | 0 | 3        | 3         | 3
3 | 1 | 3        | 3         | 2

time: O(n)
space: O(1)
"""

class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_left = 0
        max_right = 0
        result = 0
        while l < r:
            if height[l] < height[r]:
                max_left = max(max_left, height[l])
                result += max_left - height[l]
                l += 1
            else:
                max_right = max(max_right, height[r])
                result += max_right - height[r]
                r -= 1
        return result

        