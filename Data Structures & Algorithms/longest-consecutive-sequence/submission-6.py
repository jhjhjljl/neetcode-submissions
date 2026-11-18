"""
{0, 3, 2, 5, 4, 6, 1}
                   i

i | longest
0 | 1
0 | 2
0 | 3
...
0 | 7

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        n = len(nums)
        longest = 0
        for x in nums:
            if (x - 1) in nums:
                continue
            current = 1
            while (x + current) in nums:
                current += 1
            longest = max(longest, current)
        return longest

        