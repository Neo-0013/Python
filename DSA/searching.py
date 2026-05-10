# searching.py
# Beginner-friendly searching algorithms in Python

# Linear Search
def linear_search(arr, target):
    """
    Searches for target in arr using linear search.
    Returns the index if found, else -1.
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Binary Search (works only on sorted arrays)
def binary_search(arr, target):
    """
    Searches for target in arr using binary search.
    Returns the index if found, else -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Example usage
if __name__ == "__main__":
    numbers = [5, 10, 15, 20, 25, 30]

    # Linear Search
    print("Linear Search:")
    print("Index of 20:", linear_search(numbers, 20))   # Output: 3
    print("Index of 100:", linear_search(numbers, 100)) # Output: -1

    # Binary Search
    print("\nBinary Search:")
    print("Index of 25:", binary_search(numbers, 25))   # Output: 4
    print("Index of 7:", binary_search(numbers, 7))     # Output: -1
