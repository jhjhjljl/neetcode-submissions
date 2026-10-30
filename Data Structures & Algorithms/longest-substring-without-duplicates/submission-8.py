"""

r - l + 1
longest 5

hs {d, e, a, c}


b c a a b c d e a c
            l
                  r   

while s[r] is in hs, remove the s[l] from hs, then increment left counter by one

then we add s[r] into hs
then we can calculate the size of the width

time complexity: o(n)
space complexity: o(1)
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        l = 0
        longest = 0
        hs = set()
        for r in range(n):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

        