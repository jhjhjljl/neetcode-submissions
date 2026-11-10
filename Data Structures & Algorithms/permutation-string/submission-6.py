"""
s1 = "abc"
s2 = "lecabee"

7 - 3 = 4

lecabee
    l r


l | r | window | valid 
1 | 3 | eca    | x 
2 | 4 | cab    | o -> answer
3 | 5 | abe    | x
4 | 6 | bee    | x
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        if s1_len > s2_len:
            return False
        s1_counter = [0] * 26
        s2_counter = [0] * 26
        for i in range(s1_len):
            s1_counter[ord(s1[i]) - ord("a")] += 1
            s2_counter[ord(s2[i]) - ord("a")] += 1
        if s1_counter == s2_counter:
            return True
        for i in range(1, s2_len - s1_len + 1):
            char_to_remove = ord(s2[i - 1]) - ord("a")
            char_to_add = ord(s2[i + s1_len - 1]) - ord("a")
            s2_counter[char_to_remove] -= 1
            s2_counter[char_to_add] += 1
            if s1_counter == s2_counter:
                return True
        return False
        
        