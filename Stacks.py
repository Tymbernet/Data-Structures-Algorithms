
stack = []

# Push
stack.append(1)
stack.append(2)
stack.append(3)

# Peek
print("Peek:")
print(stack[-1]) # 3

# Pop
print("Pop:")
print(stack.pop()) # 3

# Peek
print("Peek:")
print(stack[-1]) # 3

# IsEmpty
print("IsEmpty:")
print(len(stack) == 0) # False

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, stack):
        self.stack.append(stack)
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
print(stack.peek()) # 20
print(stack.pop())  # 20
print(stack.is_empty())  # False
print(stack.size()) # 1
print(stack.pop())  # 10
print(stack.is_empty())  # True

from collections import deque

stack = deque()
stack.append("x")
stack.append("y")
print(stack.pop())   # y
