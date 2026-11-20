class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_spd = []
        for i in range(len(position)):
            pos_spd.append([position[i], speed[i]])
        pos_spd.sort(key = lambda x: x[0], reverse=True)
        for pos, spd in pos_spd:
            time = (target - pos) / spd
            if not stack:
                stack.append(time)
            else:
                if time > stack[-1]:
                    stack.append(time)
        return len(stack)
        