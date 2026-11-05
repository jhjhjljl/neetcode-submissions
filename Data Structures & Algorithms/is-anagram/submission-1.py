"""
counts_s = [0, 0, 0, 0, ...]
counts_t = [0, 0, 0, 0, ...]

time complexity: O(n)
space complexity: O(1)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts_s = {}
        counts_t = {}
        for i in range(len(s)):
            counts_s[s[i]] = counts_s.get(s[i], 0) + 1
            counts_t[t[i]] = counts_t.get(t[i], 0 ) + 1
        return counts_s == counts_t

        