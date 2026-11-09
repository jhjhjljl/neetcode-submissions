"""
c d v d f
    l
        r

l | r | unique_chars | r - l + 1 | longest 
c | c | c            | 1         | 1
c | d | c, d         | 2         | 2
c | v | c, d, v      | 3         | 3
c | d | d, v         |           | 3  
d | d | v            |           | 3
v | d | v, d         | 2         | 3

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        n = len(s)
        unique_chars = set()
        longest = 0
        for r in range(n):
            while l < n and s[r] in unique_chars:
                unique_chars.remove(s[l]) 
                l += 1
            unique_chars.add(s[r])
            longest = max(longest, r - l + 1)
        return longest
            
        