"""
Topic: Loops
Description: for loops, while loops, break, continue, range()
"""

# --- for loop ---
for i in range(1, 6):
    print(f"Count: {i}")

# --- while loop ---
n = 5
while n > 0:
    print(n)
    n -= 1

# --- Loop with break and continue ---
for i in range(10):
    if i == 3:
        continue   # skip 3
    if i == 7:
        break      # stop at 7
    print(i)

# --- Nested loop (multiplication table) ---
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
