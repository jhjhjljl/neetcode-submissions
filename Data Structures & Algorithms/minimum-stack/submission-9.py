"""
use an additional stack to keep track of minimum numbers

let's say we push 3, 5, and 2

stack   | min_stack
3       | 3
3, 5    | 3
3, 5, 2 | 3, 2

let's say we push 3, 5, 2 and pop twice
stack   | min_stack
3       | 3
3, 5    | 3
3, 5, 2 | 3, 2
3, 5    | 3
3       | 3
remove from min stack if number popping from main stack equals the top of the min_stack.

let's try pushing 2, 0, 3, and 0, then popping twice.

stack      | min_stack
2          | 2
2, 0       | 2, 0
2, 0, 3    | 2, 0
2, 0, 3, 0 | 2, 0, 0
2, 0, 3    | 2, 0
2, 0, 3    | 2, 0

time: O(1)
space: O(n)
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if self.min_stack[-1] >= val:
                self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop() 
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
