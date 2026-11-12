"""
use stack

["1","2","+","3","*","4","-"]
                          i

i | stack
0 | [1]
1 | [1, 2]
2 | [3]
3 | [3, 3]
4 | [9] 
5 | [9, 4]
6 | [5] -> answer

time: O(n)
space: O(n)
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] not in "+-*/":
                stack.append(int(tokens[i]))
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if tokens[i] == "+":
                    stack.append(a + b)
                elif tokens[i] == "-":
                    stack.append(a - b)
                elif tokens[i] == "*":
                    stack.append(a * b)
                elif tokens[i] == "/":
                    stack.append(int(a / b))
        return stack[0]
            
        