"""
target = 10
position = [4,1,0,7]
speed = [2,2,1,1]

[[7, 1], [4, 2], [1, 2], [0, 1]]
                            i

time = (target - position) / speed

i | stack
0 | [3]
1 | [3] 
2 | [3, 4.5] 
3 | [3, 4.5, 10]
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []
        stack = []
        for i in range(len(position)):
            pos_speed.append([position[i], speed[i]])
        pos_speed = sorted(pos_speed, key = lambda x: x[0], reverse=True)
        for pos, speed in pos_speed:
            time = (target - pos) / speed
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)



        
        