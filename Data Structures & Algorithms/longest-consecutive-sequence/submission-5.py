"""
{2,20,4,10,3,4,5}
   i

2, 3, 4, 5

longest = 4
current = 4


time: o(n)
space: o(n)
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for x in nums:
            current_sequence = 1
            if x - 1 in nums:
                continue
            while x + current_sequence in nums:
                current_sequence += 1
            longest = max(longest, current_sequence)
        return longest

            
        