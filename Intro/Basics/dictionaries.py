# dictionaries.py
# Beginner-friendly examples of Python dictionaries

# Creating a dictionary
student = {
    "name": "Alice",
    "age": 20,
    "is_student": True
}

# Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))   # safer way using get()

# Updating values
student["age"] = 21
student["course"] = "Computer Science"  # adding new key-value pair
print("Updated student:", student)

# Deleting values
del student["is_student"]   # remove a key
print("After deletion:", student)

# Looping through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key} -> {value}")

# Checking membership
if "name" in student:
    print("\nKey 'name' exists in dictionary")

# Dictionary methods
print("\nKeys:", list(student.keys()))
print("Values:", list(student.values()))
print("Items:", list(student.items()))

# Example usage
if __name__ == "__main__":
    # Another dictionary example
    capitals = {
        "India": "New Delhi",
        "USA": "Washington, D.C.",
        "France": "Paris"
    }

    print("\nCapitals Dictionary:", capitals)
    print("Capital of France:", capitals["France"])
