class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = []
        for c in s:
            if c.isalnum():
                s_clean.append(c.lower())
        s_clean = "".join(s_clean)
        length = len(s_clean)
        right = length - 1
        for left in range(length):
            if s_clean[left] != s_clean[right]:
                return False
            right -= 1
        return True


        

        