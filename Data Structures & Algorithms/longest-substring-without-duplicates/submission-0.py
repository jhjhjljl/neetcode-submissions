class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        hs = set()
        l = 0
        n = len(s)
        for r in range(n):
            while s[r] in hs:
                hs.remove(s[l])
                l += 1
            w = r - l + 1
            longest = max(longest, w)
            hs.add(s[r])
        return longest

            