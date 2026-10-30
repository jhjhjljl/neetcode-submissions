class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        counts = [0] * 26
        max_freq = 0
        l = 0
        for r in range(len(s)):
            char_index = ord(s[r]) - ord("A")
            counts[char_index] += 1
            max_freq = max(max_freq, counts[char_index])
            print(max_freq)
            while (r - l + 1) - max_freq > k:
                counts[ord(s[l]) - ord("A")] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest