"""
Problem: Find the largest number in a list without using max()
Difficulty: Easy
"""

def find_largest(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

print(find_largest([3, 7, 1, 9, 4]))  # 9
