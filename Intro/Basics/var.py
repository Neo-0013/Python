"""
Topic: Variables & Data Types
Author: Neo-0013
Description: Introduction to Python variables and built-in data types.
"""

# --- Basic Data Types ---
name = "Neo"           # str
age = 20               # int
gpa = 9.5              # float
is_student = True      # bool

# --- Type Checking ---
print(type(name))      # <class 'str'>
print(type(age))       # <class 'int'>

# --- String Operations ---
print(f"Hello, {name}! You are {age} years old.")
print(name.upper())
print(len(name))

# --- Multiple Assignment ---
x = y = z = 0
a, b, c = 1, 2, 3
