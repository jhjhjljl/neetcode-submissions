"""
s1 = "abc"
s2 = "lecabee"


counts_s1 = {
    a: 1,
    b: 1,
    c: 1
}

l e c a b e e
l   r           { l: 1, e: 1, c: 1 }
  l   r         { e: 1, c: 1, a: 1 }
    l   r       { c: 1, a: 1, b: 1 }    found
      l   r     { a: 1, b: 1, e: 1 }
        l   r   { b: 1, e: 2 }

for r starting from length of s1, upto length of s2:
    add s[r] from count
    remove s[l] from count
    if count_1 equals count_2:
        return true
    increment l

time complexity: O(n)
space complexity: O(1) -> upto 26. not infinite
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts_s1 = [0] * 26
        counts_s2 = [0] * 26
        for i in range(len(s1)):
            counts_s1[ord(s1[i]) - ord("a")] += 1
            counts_s2[ord(s2[i]) - ord("a")] += 1
        if counts_s1 == counts_s2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            counts_s2[ord(s2[l]) - ord("a")] -= 1
            counts_s2[ord(s2[r]) - ord("a")] += 1
            if counts_s2 == counts_s1:
                return True
            l += 1
        return False
        