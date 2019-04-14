class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if self.size() == 0:
            return None # если стек пустой
        else:
            q = self.stack[self.size() - 1]
            del self.stack[self.size() - 1]
            return q

    def push(self, value):
        self.stack.append(value)

    def peek(self):
        if self.size() == 0:
            return None # если стек пустой
        else:
            return self.stack[self.size() - 1]
