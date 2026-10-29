class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = []
        for c in s:
            if c.isalnum():
                s_clean.append(c.lower())
        return s_clean == s_clean[::-1]