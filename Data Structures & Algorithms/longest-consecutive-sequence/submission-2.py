"""
[2, 20, 4, 10, 3, 4, 5]

[2, 3, 4, 4, 5, 10, 20]
                     i

longest = 4
current = 1


"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        current = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue
            if nums[i] - nums[i - 1] == 1:
                current += 1
                longest = max(longest, current)
            else:
                current = 1
        return longest
        
        