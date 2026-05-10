# functions.py
# Beginner-friendly examples of Python functions

# Simple function
def greet(name):
    return f"Hello, {name}!"

# Function with multiple parameters
def add_numbers(a, b):
    return a + b

# Function with default argument
def power(base, exponent=2):
    return base ** exponent

# Function with keyword arguments
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

# Function returning multiple values
def calculate(a, b):
    sum_val = a + b
    diff_val = a - b
    return sum_val, diff_val

# Recursive function (factorial)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    print(greet("Neo"))                  # Output: Hello, Neo!
    print("Sum:", add_numbers(10, 5))    # Output: 15
    print("Power:", power(3))            # Output: 9
    print("Power:", power(2, 5))         # Output: 32
    introduce("Alice", 20)               # Output: My name is Alice and I am 20 years old.
    s, d = calculate(15, 5)
    print("Sum:", s, "Difference:", d)   # Output: Sum: 20 Difference: 10
    print("Factorial of 5:", factorial(5))  # Output: 120
