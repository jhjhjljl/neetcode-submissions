"""
current width can be calculated: r - l + 1
longest = max(longest, r - l + 1)

while s[r] is in hs:
    remove s[l] from hs
    move l + 1

add s[r] to hs
re-calculate longest
move r + 1


longest = 3
hs = {b, c, a}


[a b c a d d c a c d b]
   l   r
"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        longest = 0
        l = 0
        r = 0
        n = len(s)
        while r < n:
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest
        