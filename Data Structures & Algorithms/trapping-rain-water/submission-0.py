class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        max_left = [0] * length
        max_right = [0] * length
        diff = [0] * length
        result = 0
        current_max_left = height[0]
        current_max_right = height[-1]
        for i in range(1, length):
            max_left[i] = current_max_left
            current_max_left = max(current_max_left, height[i])
        for i in range(length - 2, -1, -1):
            max_right[i] = current_max_right
            current_max_right = max(current_max_right, height[i])
        for i in range(length):
            diff[i] = min(max_left[i], max_right[i]) - height[i]
            if diff[i] < 0:
                diff[i] = 0
        for x in diff:
            result += x
        return result
