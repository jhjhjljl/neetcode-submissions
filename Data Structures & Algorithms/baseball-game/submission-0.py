"""
["1","2","+","C","5","D"]
                      i

i | stack         | result
0 | [1]           | 1 
1 | [1, 2]        | 3
2 | [1, 2, 3]     | 6
3 | [1, 2]        | 3
4 | [1, 2, 5]     | 8
5 | [1, 2, 5, 10] | 18
"""

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for x in operations:
            if x == "+":
                stack.append(stack[-1] + stack[-2])
            elif x == "D":
                stack.append(stack[-1] * 2)
            elif x == "C":
                stack.pop()
            else:
                stack.append(int(x))
        return sum(stack)
        