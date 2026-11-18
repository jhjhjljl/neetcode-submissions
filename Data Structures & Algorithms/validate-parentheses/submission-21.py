class Solution:
    def isValid(self, s: str) -> bool:
        matching_pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c not in matching_pairs:
                stack.append(c)
            else:
                if stack and stack[-1] == matching_pairs[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
            

        