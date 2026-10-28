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
