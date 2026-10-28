class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        longest = 0
        l = 0
        n = len(s)
        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest

