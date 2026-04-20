class MinStack:
    

    def __init__(self):
        self.stack=[]
        self.min_prefix=[] # Represents the "min so far"

    def push(self, val: int) -> None:
        if not self.min_prefix or val < self.min_prefix[-1]:
            self.min_prefix.append(val)
        else:
            self.min_prefix.append(self.min_prefix[-1])
        self.stack.append(val)

    def pop(self) -> None:
        self.min_prefix.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_prefix[-1]
        
