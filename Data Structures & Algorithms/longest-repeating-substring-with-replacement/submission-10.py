"""
k = 1
AACBABB
   l
      r

l | r | current_window | counts          | result
0 | 0 | 1              | A: 1            | 1
0 | 1 | 2              | A: 2            | 2
0 | 2 | 3              | A: 2 C: 1       | 3
0 | 3 | 4              | A: 2 C: 1 B: 1  | 3
1 | 3 | 3              | A: 1 C: 1 B: 1  | 3
2 | 3 | 2              | C: 1 B: 1       | 3
2 | 4 | 3              | A: 1 C: 1 B: 1  | 3
3 | 4 | 2              | A: 1 B: 1       | 3
3 | 5 | 3              | A: 1 B: 2       | 3
3 | 6 | 4              | A: 1 B: 3       | 4
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        left = 0
        counts = {}
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result

        