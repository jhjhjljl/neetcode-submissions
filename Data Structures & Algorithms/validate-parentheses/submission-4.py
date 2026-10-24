class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        close_open_hm = {
            "]": "[",
            ")": "(",
            "}": "{"
        }

        for c in s:
            if c not in close_open_hm:
                stack.append(c)
            else:
                if stack and close_open_hm[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False
