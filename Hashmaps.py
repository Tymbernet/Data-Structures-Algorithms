# Hashmaps in Python — very simple
# Python uses dictionaries for hashmaps.

# 1. Create le dictionary
grade_book = {
    "John Kaisen": "A",
    "John Zenin" : "A+"
}

print("grade_book:", grade_book)

# 2. Add a new key/value pair
grade_book["Satoru Gojo"] = "A++"
print("after add:", grade_book)

# 3. Look up a value by key
print("John Kaisen's grade:", grade_book["John Kaisen"])

# 4. Delete a pair by key
del grade_book["John Kaisen"]
print("after delete:", grade_book)

# 5. Pairing: keys and values stay linked
for name, grade in grade_book.items():
    print(name, "->", grade)

# 6. If a key is missing, .get() can return a default instead of raising an error.
print("Itadori's grade:", grade_book.get("Itadori", "not found"))

