class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for x in s:
            if x not in bracket_map:
                stack.append(x)
            else:
                if stack and stack[-1] == bracket_map[x]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
        