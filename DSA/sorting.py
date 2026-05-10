# sorting.py
# Beginner-friendly sorting algorithms in Python

# Bubble Sort
def bubble_sort(arr):
    """
    Bubble Sort repeatedly swaps adjacent elements
    if they are in the wrong order.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# Insertion Sort
def insertion_sort(arr):
    """
    Insertion Sort builds the sorted array one item at a time.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Quick Sort
def quick_sort(arr):
    """
    Quick Sort uses divide and conquer.
    Picks a pivot and partitions the array.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# Example usage
if __name__ == "__main__":
    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Original List:", numbers)

    print("\nBubble Sort:", bubble_sort(numbers.copy()))
    print("Insertion Sort:", insertion_sort(numbers.copy()))
    print("Quick Sort:", quick_sort(numbers.copy()))
