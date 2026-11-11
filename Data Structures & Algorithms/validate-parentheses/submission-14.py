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
5 | 

[(])
  i

i | stack
0 | [
1 | [, ( 
2 | [, ( -> invalid

time: O(n)
space: O(n)

"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        closing_opening_pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c in closing_opening_pairs:
                if stack and stack[-1] == closing_opening_pairs[c]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False

                
        