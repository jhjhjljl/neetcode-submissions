class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        max_left = height[0]
        max_right = height[length - 1]
        max_left_arr = [0] * length
        max_right_arr = [0] * length
        min_left_right_arr = [0] * length
        diff = [0] * length
        for i in range(1, length):
            max_left_arr[i] = max_left
            max_left = max(max_left, height[i])
        for i in range(length - 2, -1, -1):
            max_right_arr[i] = max_right
            max_right = max(max_right, height[i])
        for i in range(length):
            min_left_right_arr[i] = min(max_left_arr[i], max_right_arr[i])
        for i in range(length):
            diff[i] = min_left_right_arr[i] - height[i]
            if diff[i] < 0:
                diff[i] = 0
        result = 0
        for x in diff:
            result += x
        return result

        