# Control-flow.py
# Beginner-friendly examples of control flow in Python

# If-Else Example
def check_number(num):
    if num > 0:
        print(f"{num} is Positive")
    elif num == 0:
        print("Number is Zero")
    else:
        print(f"{num} is Negative")


# For Loop Example
def print_numbers(n):
    print("Printing numbers from 1 to", n)
    for i in range(1, n + 1):
        print(i)


# While Loop Example
def countdown(start):
    print("Countdown starts:")
    while start > 0:
        print(start)
        start -= 1
    print("Blast off!")


# Break and Continue Example
def demo_break_continue():
    print("Demo of break and continue:")
    for i in range(1, 10):
        if i == 5:
            print("Breaking at", i)
            break
        if i % 2 == 0:
            continue  # Skip even numbers
        print("Odd number:", i)


# Example usage
if __name__ == "__main__":
    check_number(10)
    check_number(-3)
    check_number(0)

    print_numbers(5)

    countdown(3)

    demo_break_continue()
