# string_methods.py
# A beginner-friendly guide to Python string methods

# Let's start with a sample string
text = "Hello, Python Learners!"

# 1. Changing case
print("Original:", text)
print("Lowercase:", text.lower())   # Converts all letters to lowercase
print("Uppercase:", text.upper())   # Converts all letters to uppercase
print("Title Case:", text.title())  # Capitalizes each word

# 2. Stripping whitespace
extra_spaces = "   Neo is coding   "
print("With spaces:", extra_spaces)
print("Stripped:", extra_spaces.strip())  # Removes spaces from both ends

# 3. Splitting and joining
words = text.split(" ")   # Splits string into a list by spaces
print("Split into words:", words)

joined = "-".join(words)  # Joins list back into a string with '-'
print("Joined with '-':", joined)

# 4. Finding and replacing
print("Find 'Python':", text.find("Python"))   # Returns index of substring
print("Replace 'Python' with 'World':", text.replace("Python", "World"))

# 5. Checking string content
print("Is alphabetic?", "Neo".isalpha())   # True if all characters are letters
print("Is numeric?", "123".isdigit())      # True if all characters are digits
print("Is alphanumeric?", "Neo123".isalnum())  # True if letters + numbers

# 6. Startswith / Endswith
print("Starts with 'Hello'?", text.startswith("Hello"))
print("Ends with 'Learners!'?", text.endswith("Learners!"))

# 7. Counting occurrences
print("Count of 'e':", text.count("e"))

# 8. Indexing and slicing
print("First character:", text[0])       # Indexing
print("First 5 characters:", text[:5])   # Slicing

# 9. Formatting strings
name = "Neo"
age = 20
print("Formatted string:", f"My name is {name} and I am {age} years old.")

# 10. Useful check
empty = ""
print("Is empty string?", empty == "")
