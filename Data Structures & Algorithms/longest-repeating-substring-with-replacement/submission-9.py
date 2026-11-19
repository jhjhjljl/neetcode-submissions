"""
AAACBABB
   l
       r

l | r | window_size | count
0 | 0 | 1           | A: 1
0 | 1 | 2           | A: 2
0 | 2 | 3           | A: 3
0 | 3 | 4           | A: 3, C: 1
0 | 4 | 5           | A: 3, C: 1 B: 1
0 | 5 | 6           | A: 4, C: 1 B: 1
0 | 6 | 7           | A: 4, C: 1 B: 2 
1 | 6 | 6           | A: 3, C: 1 B: 2 
2 | 6 | 5           | A: 2, C: 1 B: 2 
3 | 6 | 4           | A: 1, C: 1 B: 2 
3 | 7 | 5           | A: 1, C: 1 B: 3 



"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        max_length = 0
        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)
        return max_length
            


        