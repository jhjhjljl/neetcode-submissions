"""
abcabcbb
l
   r

l | r | current_window
0 | 0 | {a}
0 | 1 | {a, b}
0 | 2 | {a, b, c}
0 | 3 | {a, b, c}
1 | 3 | {a, b, c}
1 | 4 | {a, b, c}
2 | 4 | {a, b, c}
2 | 5 | {a, b, c}
3 | 5 | {a, b, c}
3 | 5 | {a, b, c}
3 | 6 | {a, b, c}
4 | 6 | {b, c}
5 | 6 | {c, b}

"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left += 1
            window.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length


        