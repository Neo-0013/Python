#PYTHON INTRODUCTION

This file is a concise, practical Python basics guide you can keep in your repo as basics.md. It covers the essential syntax and concepts every beginner should know, with clear examples and small exercises you can copy and run. Use this as the foundation for your documentation and expand each section into its own file later.

Setup and First Program
Install Python from the official site or your package manager. Verify installation in a terminal:

bash
python --version
Run a script

bash
# Save this as hello.py and run
print("Hello, World!")
Run interactively

bash
python
# then type Python code directly
Core Concepts
Variables and Data Types
Python is dynamically typed. Common types are int, float, str, and bool.

python
name = "Joe"
age = 17
height = 5.9
is_student = True

print(name, age, height, is_student)
print(f"{name} is {age} years old. Student: {is_student}")
Tip Use descriptive variable names.

Comments
Single line comments start with #. Use comments to explain why code exists.

python
# This is a single line comment

"""
This is a multi-line string.
It can be used as a block comment.
"""
Input and Output
Get user input and print formatted output.

python
user = input("Enter your name: ")
print("Hello,", user)
# or formatted
print(f"Welcome, {user}!")
Operators
Arithmetic, comparison, logical, and assignment operators.

python
# Arithmetic
a = 10
b = 3
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)

# Comparison
print(a > b, a == b, a != b)

# Logical
print(a > 5 and b < 5, not (a < b))

# Assignment
a += 2  # same as a = a + 2
Control Flow and Loops
If Else
python
x = 10
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
For Loop
Iterate over ranges and collections.

python
for i in range(5):
    print(i)

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
While Loop
python
count = 0
while count < 5:
    print(count)
    count += 1
List Comprehension
Compact way to build lists.

python
squares = [x * x for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
Functions and Modules
Defining Functions
python
def greet(name):
    """Return a greeting string for name."""
    return f"Hello, {name}!"

print(greet("Joe"))
Arguments and Defaults
python
def power(base, exponent=2):
    return base ** exponent

print(power(3))      # 9
print(power(2, 3))   # 8
Variable Arguments
python
def summarize(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

summarize(1, 2, a=3, b=4)
Modules and Imports
Create reusable code in separate files.

python
# mymodule.py
def hello():
    return "Hello from mymodule"

# main.py
import mymodule
print(mymodule.hello())
Use from module import name for direct access.

Data Structures Examples and Exercises
Lists
Ordered, mutable collection.

python
numbers = [1, 2, 3]
numbers.append(4)
numbers[0] = 10
print(numbers)
Tuples
Ordered, immutable collection.

python
coords = (10, 20)
# coords[0] = 5  # error
Dictionaries
Key value mapping.

python
student = {"name": "Joe", "age": 17}
print(student["name"])
student["grade"] = "A"
Sets
Unordered collection of unique items.

python
s = {1, 2, 3, 3}
s.add(4)
print(s)  # {1,2,3,4}
Useful Built Ins
python
len([1,2,3])
sum([1,2,3])
min([1,2,3])
max([1,2,3])
sorted([3,1,2])
Small Projects and Exercises
Work through these to solidify basics. Put solutions in projects/ or a solutions/ folder.

Hello and Input

Write a script that asks for the user's name and age and prints a friendly message.

Simple Calculator

Create a program that reads two numbers and prints their sum, difference, product, and quotient.

Word Counter

Read a text file and count how many times each word appears.

Number Filter

Given a list of numbers, produce a new list with only even numbers using list comprehension.

Contacts Dictionary

Build a small contacts manager using a dictionary. Support add, remove, and lookup operations.

Mini Quiz

Create a short quiz that asks 3 questions, collects answers, and shows the score.

Next Steps
After mastering these basics, continue with:

File Handling read and write files safely with with open.

Error Handling use try, except, finally.

Object Oriented Programming classes, methods, inheritance.

Virtual Environments use venv and pip for dependencies.

Testing write simple tests with unittest or pytest.
