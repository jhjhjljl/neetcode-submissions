"""
use sliding window
make window valid
as long as window is valid, move right pointer
if the window is invalid, move the left pointer until the window is valid

pwwkew
  l
     r

l | r | seen    | r - l + 1 | longest
p | p | p       | 1         | 1
p | w | p, w    | 2         | 2
p | w | w       |           |
w | w |         |           |
w | w | w       | 1         | 2
w | k | w, k    | 2         | 2
w | e | w, k, e | 3         | 3 

time: O(n)
space: O(1)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        seen = set()
        for r in range(len(s)):
            while l < r and s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

        