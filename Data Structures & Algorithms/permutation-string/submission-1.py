"""
s1 = "abc"
s2 = "lecabee"

lecabee
    i 

i | window | valid
0 | lec    | x
1 | eca    | x
2 | cab    | o
3 | abe    | x 
4 | bee    | x

time: O(n)
space: O(1)
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        if s1_length > s2_length:
            return False
        s1_counter = {}
        s2_counter = {}
        for i in range(s1_length):
            s1_counter[s1[i]] = s1_counter.get(s1[i], 0) + 1
            s2_counter[s2[i]] = s2_counter.get(s2[i], 0) + 1
        if s1_counter == s2_counter:
            return True
        for i in range(1, s2_length - s1_length + 1):
            s2_counter[s2[i - 1]] = s2_counter.get(s2[i - 1], 0) - 1
            if s2_counter[s2[i - 1]] == 0:
                del s2_counter[s2[i - 1]]
            right_char = s2[i + s1_length - 1]
            s2_counter[right_char] = s2_counter.get(right_char, 0) + 1 
            if s1_counter == s2_counter:
                return True
        return False


            

        

        