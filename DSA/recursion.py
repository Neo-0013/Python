"""
Topic: Recursion
Description: Understanding recursion with classic examples
"""

# --- Factorial ---
def factorial(n):
    if n == 0 or n == 1:   # base case
        return 1
    return n * factorial(n - 1)  # recursive call

print(factorial(5))   # 120

# --- Fibonacci ---
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

for i in range(8):
    print(fibonacci(i), end=" ")  # 0 1 1 2 3 5 8 13

# --- Sum of list recursively ---
def sum_list(lst):
    if not lst:
        return 0
    return lst[0] + sum_list(lst[1:])

print(sum_list([1, 2, 3, 4, 5]))  # 15
