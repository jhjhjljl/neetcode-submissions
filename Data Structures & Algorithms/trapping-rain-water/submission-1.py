class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        max_left = [0] * length
        max_right = [0] * length
        max_left_current = 0
        max_right_current = 0
        result = 0
        for i in range(0, length):
            max_left[i] = max_left_current
            max_left_current = max(max_left_current, height[i])
        for i in range(length - 1, -1, -1):
            max_right[i] = max_right_current
            max_right_current = max(max_right_current, height[i])
        for i in range(length):
            diff = min(max_left[i], max_right[i]) - height[i]
            if diff < 0:
                diff = 0
            result += diff
        return result
        
        
