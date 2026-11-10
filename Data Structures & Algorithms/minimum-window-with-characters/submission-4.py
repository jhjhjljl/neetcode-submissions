"""
use sliding window, it's opposite of traditional sliding window

we increase the size of the window when it's invalid
we decrease the size of the window when it's valid - so that we get minimal length

s = "OUZODYXAZV"
t = "XYZ"

OUZODYXAZV
      l
         r


l | r | current_window | valid | shortest
0 | 0 | O              | x     | -
0 | 1 | OU             | x     | -
0 | 2 | OUZ            | x     | - 
0 | 3 | OUZO           | x     | -
0 | 4 | OUZOD          | x     | -
0 | 5 | OUZODY         | x     | -
0 | 6 | OUZODYX        | o     | 7
1 | 6 | UZODYX         | o     | 6
2 | 6 | ZODYX          | o     | 5
3 | 6 | ODYX           | x     | 5
3 | 7 | ODYXA          | x     | 5
3 | 8 | ODYXAZ         | o     | 5
4 | 8 | DYXAZ          | o     | 5
5 | 8 | YXAZ           | o     | 4 -> answer
6 | 8 | XAZ            | x     | 4
6 | 9 | XAZV           | x     | 4

time: O(n)
space: O(1)
"""

class Solution:
    def is_valid(self, s_counter: dict, t_counter: dict) -> bool:
        for key, val in t_counter.items():
            if key not in s_counter or s_counter[key] < val:
                return False
        return True
    
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        t_counter = {}
        for c in t:
            t_counter[c] = t_counter.get(c, 0) + 1
        shortest = float("inf")
        n = len(s)
        l = 0
        min_l = 0
        min_r = 0
        s_counter = {}
        for r in range(n):
            s_counter[s[r]] = s_counter.get(s[r], 0) + 1
            while l <= r and self.is_valid(s_counter, t_counter):
                if (r - l + 1) < shortest:
                    min_l = l
                    min_r = r
                    shortest = min(shortest, r - l + 1)
                s_counter[s[l]] -= 1
                l += 1
        if shortest == float("inf"):
            return ""
        return s[min_l:min_r + 1]


            

            
        