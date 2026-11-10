"""
k = 1
AAABABB
l
     r

l | r | seen             | window_size | longest | valid
0 | 0 | A: 1             | 1           | 1       | o
0 | 1 | A: 2             | 2           | 2       | o
0 | 2 | A: 3             | 3           | 3       | o
0 | 3 | A: 3, B: 1       | 4           | 4       | o
0 | 4 | A: 4, B: 1       | 5           | 5       | o
0 | 5 | A: 4, B: 2       | 6           | 5       | x
1 | 5 | A: 3, B: 2       | 5           | 5       | x
2 | 5 | A: 2, B: 2       | 4           | 5       | x
3 | 5 | A: 1, B: 2       | 3           | 5       | o
3 | 6 | A: 1, B: 3       | 4           | 5       | o

time: O(n)
space: O(1)
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        longest = 0
        counter = {}
        for right, char in enumerate(s):
            counter[char] = counter.get(char, 0) + 1
            while (right - left + 1) - max(counter.values()) > k:
                counter[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest


            
            


        