# Linear Search: look at each number one by one
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # if found, return index
    return -1  # not found

# Binary Search: smart search on sorted list
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Our list of numbers
arr = [7, 9, 12, 21, 27, 35, 47, 53, 5, 54]

# Ask the user what number to find
target = int(input("Enter the number to search: "))

# Linear Search (one-by-one)
result_linear = linear_search(arr, target)
print("Linear Search result:", result_linear if result_linear != -1 else "Not found")

# Binary Search needs a sorted list
sorted_arr = sorted(arr)
result_binary = binary_search(sorted_arr, target)
print("Binary Search result (in sorted list):", result_binary if result_binary != -1 else "Not found")
