class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop(0)

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
    
stack = Stack()
stack.push(5)
stack.push(3)
stack.push(4)
stack.push(6)
stack.push(1)
print(stack.pop())
print(stack.pop())
print(stack.is_empty())