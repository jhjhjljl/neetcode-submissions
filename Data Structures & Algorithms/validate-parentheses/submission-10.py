class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if stack and ((c == ")" and stack[-1] == "(") or \
                    (c == "]" and stack[-1] == "[") or \
                    (c == "}" and stack[-1] == "{")):
                    stack.pop()
                    continue
                else:
                    return False
        return True if not stack else False
                