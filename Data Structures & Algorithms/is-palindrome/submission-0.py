"""
reverse string.

time: O(n)
space: O(n)
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_alnum = []
        for c in s:
            if not c.isalnum():
                continue
            s_alnum.append(c.lower())
        return s_alnum == s_alnum[::-1]
        