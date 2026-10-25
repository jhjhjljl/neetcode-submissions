class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for x in nums:
            if x - 1 not in nums:
                current = 1
                while (x + current) in nums:
                    current += 1
                longest = max(longest, current)
        return longest