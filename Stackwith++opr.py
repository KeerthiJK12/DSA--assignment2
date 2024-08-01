class CustomStack:
    def __init__(self, maxSize):
        self.stack = []
        self.incremental = []
        self.maxSize = maxSize

    def push(self, x):
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.incremental.append(0)

    def pop(self):
        if not self.stack:
            return -1
        if len(self.stack) > 1:
            self.incremental[-2] += self.incremental[-1]
        result = self.stack.pop() + self.incremental.pop()
        return result

    def increment(self, k, val) :
        if self.stack:
            idx = min(k, len(self.stack)) - 1
            self.incremental[idx] += val


customStack = CustomStack(5)
customStack.push(1)
customStack.push(2)
print(customStack.pop())  
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.increment(3, 100)
customStack.increment(2, 100)
print(customStack.pop())  
print(customStack.pop()) 

