from collections import deque

queue = deque()

# Enqueue
queue.append("a")
queue.append("b")
queue.append("c")

# Peeking at the front
print(queue[0])

print(queue.popleft())  # dequeue -> a
print(len(queue))       # size -> 2

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, queue):
        self.queue.append(queue)
    
    def dequeue(self):
        return self.queue.pop(0)
    
    def peek(self):
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)