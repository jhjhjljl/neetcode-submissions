"""
use stack

([{}])
     i

i | stack 
0 | (
1 | (, [
2 | (, [, {
3 | (, [
4 | (
5 | "" - valid


"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        pairs = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        stack = []
        for c in s:
            if c in pairs:
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
                
        