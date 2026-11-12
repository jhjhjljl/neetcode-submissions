"""
[30,38,30,36,35,40,28]
                    i
 
 i | stack      | result
 0 | [0]        | [0, 0, 0, 0, 0, 0, 0]
 1 | [1]        | [1, 0, 0, 0, 0, 0, 0]
 2 | [1, 2]     | [1, 0, 0, 0, 0, 0, 0]
 3 | [1, 3]     | [1, 0, 1, 0, 0, 0, 0]
 4 | [1, 3, 4]  | [1, 0, 1, 0, 0, 0, 0]
 5 | [5]        | [1, 4, 1, 2, 1, 0, 0]
 6 | [5, 6]     | [1, 4, 1, 2, 1, 0, 0]

time: O(n)
space: O(n)

"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, x in enumerate(temperatures):
            if i == 0:
                stack.append(i)
                continue
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            stack.append(i)
        return result
            

        