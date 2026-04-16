from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Traversal
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Traversal

def bfs(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

bfs(root)

# Preorder DFS -> used when you need to copy/serialize a Tree
def preorder_dfs(root):
    if not root:
        return
    
    print(root.val)
    preorder_dfs(root.left)
    preorder_dfs(root.right)

# Inorder DFS -> used when a Tree is a BST, 
# or when it gives a sorted order
def inorder_dfs(root):
    if not root:
        return
    inorder_dfs(root.left)
    print(root.val)
    inorder_dfs(root.right)

# PostOrder DFS -> you need results from children b4 parents
def postorder_dfs(root):
    if not root:
        return
    
    postorder_dfs(root.left)
    postorder_dfs(root.right)
    print(root.val)