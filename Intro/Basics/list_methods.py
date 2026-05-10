# list_methods.py
# Beginner-friendly guide to Python list methods

# Sample list
fruits = ["apple", "banana", "cherry"]

# 1. Append - add item at the end
fruits.append("orange")
print("After append:", fruits)

# 2. Insert - add item at specific position
fruits.insert(1, "grape")
print("After insert:", fruits)

# 3. Remove - delete first occurrence of item
fruits.remove("banana")
print("After remove:", fruits)

# 4. Pop - remove item at index (default: last)
popped_item = fruits.pop()
print("Popped item:", popped_item)
print("After pop:", fruits)

# 5. Index - find position of item
print("Index of cherry:", fruits.index("cherry"))

# 6. Count - number of occurrences
fruits.append("apple")
print("Count of apple:", fruits.count("apple"))

# 7. Sort - arrange items
fruits.sort()
print("Sorted list:", fruits)

# 8. Reverse - reverse order
fruits.reverse()
print("Reversed list:", fruits)

# 9. Copy - shallow copy of list
copy_list = fruits.copy()
print("Copied list:", copy_list)

# 10. Clear - remove all items
fruits.clear()
print("After clear:", fruits)
