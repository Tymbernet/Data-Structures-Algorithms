# Linked Lists

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Traversal
head = Node(1)
head.next = Node(2)

curr = head
while curr:
    print(curr.val)
    curr = curr.next
    
# Insertion
head = Node(1)
head.next = Node(3)
new_node = Node(2)
new_node.next = head.next
head.next = new_node

# Deletion
head = Node(1)
head.next = Node(2)
head.next = head.next.next

# Reversal
head = Node(1)
head.next = Node(2)
prev = None
curr = head

while curr:
    next_node = curr.next
    curr.next = prev
    prev = curr
    curr = next_node
    head = prev

# Double Linked List

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

