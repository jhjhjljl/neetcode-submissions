class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            min_idx = i
            min_val = nums[min_idx]
            for j in range(i+1, len(nums)):
                if nums[j] < min_val:
                    min_idx = j
                    min_val = nums[min_idx]
            nums[min_idx] = nums[i]
            nums[i] = min_val
        return nums



        