"""
s1 = abc
s2 = lecabee

lecabee
i

i | sorted_window | valid
0 | cel           | x
1 | ace           | x
2 | abc           | o
3 | abe           | x 
4 | bee           | x

time: O(nlogn)
space: O(1)
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1 = "".join(sorted(s1))
        for i in range(len(s2) - len(s1) + 1):
            current_window = s2[i:i + len(s1)]
            current_window = "".join(sorted(current_window))
            if current_window == s1:
                return True
        return False
            

        