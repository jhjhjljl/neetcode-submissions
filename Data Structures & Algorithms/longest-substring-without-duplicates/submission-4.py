"""
use sliding window to make windows valid
move right as long as valid
move left until the window is valid

time: O(n)
space: O(1)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        seen = set()
        for r in range(len(s)):
            while l < r and s[r] in seen:
                seen.remove(s[l]) 
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
        