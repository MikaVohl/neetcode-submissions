class MinStack:

    def __init__(self):
        self.stack = [] # holds (val, min)

    def push(self, val: int) -> None:
        minimum = min(val, self.getMin()) if self.stack else val
        self.stack.append((val, minimum))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
