"""
s = racecar
t = carrace

s = aaccerr
t = aaccerr
time complextiy: O(nlogn)
space complexity: O(n)
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        return s == t

        