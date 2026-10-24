class MinStack:

    def __init__(self):
        self.stack = []
        self.min_track = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.min_track[-1] if self.min_track else val)
        self.min_track.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_track.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_track[-1]
        
