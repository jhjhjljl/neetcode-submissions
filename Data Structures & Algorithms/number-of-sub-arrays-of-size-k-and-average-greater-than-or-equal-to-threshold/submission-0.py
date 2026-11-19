class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        current_sum = 0
        for i in range(k):
            current_sum += arr[i]
        if (current_sum / k) >= threshold:
            result += 1
        left = 0
        for right in range(k, len(arr)):
            current_sum += arr[right]
            current_sum -= arr[left]
            if (current_sum / k) >= threshold:
                result += 1
            left += 1
        return result
        
        