class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x == "+":
                right = stack.pop()
                stack.append(stack.pop() + right)
            elif x == "-":
                right = stack.pop()
                stack.append(stack.pop() - right)
            elif x == "*":
                stack.append(stack.pop() * stack.pop())
            elif x == "/":
                right = stack.pop()
                stack.append(int(stack.pop() / right))
            else:
                stack.append(int(x))
        return stack[0]
        