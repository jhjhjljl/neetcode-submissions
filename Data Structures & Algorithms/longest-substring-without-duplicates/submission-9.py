class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        hs = set()
        for r in range(len(s)):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
        