class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hs = set()
        l = 0
        n = len(s)
        longest = 0
        for r in range(n):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            hs.add(s[r])
            longest = max(longest, r - l + 1)
        return longest

        