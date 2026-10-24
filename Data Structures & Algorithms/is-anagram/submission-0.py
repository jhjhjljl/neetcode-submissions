"""
i will use hashmap for the solution, counting frequency of each character
in the string. then compare if two hashmap are identical.
time complexity will be o(n) where n is the length of string.
"""


from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)
        