class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        max_count = 0
        longest = 0
        l = 0
        for r in range(len(s)):
            char_index = ord(s[r]) - ord("A")
            counts[char_index] += 1
            max_count = max(max_count, counts[char_index])
            while (r - l + 1) - max_count > k:
                counts[ord(s[l]) - ord("A")] -= 1
                l += 1
            longest = max(longest, r - l + 1)
        return longest
            

        
        