
# Arrays -- Contagius memory --> slow insert/delete O(n)

arr = [1, 2, 3, 4]

# Access
print(arr[0])  # O(1)

# Append
arr.append(5)  # O(1) amortized

# Insert
arr.insert(0, 0)  # O(n)

# Pop
arr.pop()  # O(1)