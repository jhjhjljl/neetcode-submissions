class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts_1 = [0] * 26
        counts_2 = [0] * 26
        for i in range(len(s1)):
            counts_1[ord(s1[i]) - ord("a")] += 1
            counts_2[ord(s2[i]) - ord("a")] += 1
        if counts_1 == counts_2:
            return True
        l = 0
        for r in range(len(s1), len(s2)):
            counts_2[ord(s2[l]) - ord("a")] -= 1
            counts_2[ord(s2[r]) - ord("a")] += 1
            if counts_2 == counts_1:
                return True
            l += 1
        return False
        
        