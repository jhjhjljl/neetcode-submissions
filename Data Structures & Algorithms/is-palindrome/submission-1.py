"""
Was it a car or a cat I saw?
            lr

W = w
a = a
s = s

- continue on non alnum characters
- compare s[l] and s[r] at lower case version.

time: O(n)
space: O(1)

"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
        