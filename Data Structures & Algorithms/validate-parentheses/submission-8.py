class Solution:
    def isValid(self, s: str) -> bool:
        hm = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c not in hm:
                stack.append(c)
            else:
                if stack and hm[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False