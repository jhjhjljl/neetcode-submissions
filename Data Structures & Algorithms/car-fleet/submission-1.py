"""
target = 10 position = [4,1,0,7], speed = [2,2,1,1]

cars = [[4, 2], [1, 2], [0, 1], [7, 1]]
sorted
[[7, 1], [4, 2], [1, 2], [0, 1]]

i | stack
0 | 3
1 | 3 
2 | 3, 4.5
3 | 3, 4.5, 10

time: O(nlogn)
space: O(n)

[[0,4], [2,2], [[4,1]]]
[[4,1], [2,2], [0,4]]
                 i 

i | stack
0 | [96]
1 | [96] 
2 | [96] 

"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []
        cars = []
        for i in range(n):
            cars.append([position[i], speed[i]])
        cars = sorted(cars, key = lambda x: x[0], reverse=True)
        for pos, spd in cars:
            time = (target - pos) / spd
            if not stack:
                stack.append(time)
            else:
                if stack[-1] < time:
                    stack.append(time)
        return len(stack)

        