"""
s = "([{}])"

"([{}])"
"([])"
"()"
""  -> valid

s = "[(])"
"[(])" -> invalid

time: O(n^2)
space: O(n)
"""

class Solution:
    def isValid(self, s: str) -> bool:
        while "[]" in s or "{}" in s or "()" in s: 
            s = s.replace("{}", "")
            s = s.replace("[]", "")
            s = s.replace("()", "")
        return s == ""
        