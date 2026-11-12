"""
use stack

[30,38,30,36,35,40,28]
 1, 4, 1, 2, 1, 0, 0 

i | stack                          | result
0 | [[0, 30]]                      | [0, 0, 0, 0, 0, 0, 0]
1 | [[1, 38]]                      | [1, 0, 0, 0, 0, 0, 0]
2 | [[1, 38], [2, 30]]             | [1, 0, 0, 0, 0, 0, 0]
3 | [[1, 38], [3, 36]]             | [1, 0, 1, 0, 0, 0, 0]
4 | [[1, 38], [3, 36], [4, 35]]    | [1, 0, 1, 0, 0, 0, 0]
5 | [[5, 40]]                      | [1, 4, 1, 2, 1, 0, 0]
6 | [[5, 40], [6, 28]]             | [1, 4, 1, 2, 1, 0, 0]

time: O(n)
space: O(n)
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0] * n
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                prev_index, _ = stack.pop()
                result[prev_index] = i - prev_index
            stack.append([i, temp])
        return result


        