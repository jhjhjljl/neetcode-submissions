"""
use stack. whenever you see a number you push onto stack
when you see a sign, pop two numbers from stack, and push answer back to stack

["1","2","+","3","*","4","-"]
                          i

i | stack
0 | [1]
1 | [1, 2]
2 | [3]
3 | [3, 3]
4 | [9]
5 | [9, 4]
6 | [5]

time: O(n)
space: O(n)


["4","13","5","/","+"]
               i

i | stack
0 | 4
1 | 4, 13
2 | 4, 13, 5
3 | 4,  
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            x = tokens[i]
            if x not in "+-*/":
                stack.append(int(x))
            else:
                b = stack.pop()
                a = stack.pop()
                if x == "+":
                    stack.append(a + b)
                elif x == "-":
                    stack.append(a - b)
                elif x == "*":
                    stack.append(a * b)
                elif x == "/":
                    stack.append(int(a / b))
        return stack[0]
            
        