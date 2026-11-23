"""
target = 4
[1,2,3,5,6]
       l
     r
       m
l | r | m | result
0 | 4 | 2 | 3
3 | 4 | 3 | 

 
"""
class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap:
            self.timemap[key] = []
        self.timemap[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timemap:
            return ""
        if not self.timemap[key]:
            return ""
        left = 0
        right = len(self.timemap[key]) - 1
        result = ""
        while left <= right:
            mid = (left + right) // 2
            if timestamp >= self.timemap[key][mid][1]:
                result = self.timemap[key][mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return result

        
        
