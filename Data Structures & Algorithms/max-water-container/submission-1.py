"""
[1, 7, 2, 5, 4, 7, 3, 6]
    l              r

w = r - l
h = min(heights[r], heights[l])
a = w * h
1, 6 = 7 * 1 = 7 inc left
7, 6 = 6 * 6 = 36 dec right
7, 3 = 5 * 3 = 15 dec right
...

time: O(n)
space: O(1)
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            w = r - l
            h = min(heights[l], heights[r])
            a = w * h
            maximum = max(maximum, a)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maximum


        