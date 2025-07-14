# Function: Recursive Binary Search (O(log n) space)

def binary_search(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, right)
    else:
        return binary_search(arr, target, left, mid - 1)

# Test
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 14
result = binary_search(arr, target, 0, len(arr) - 1)
print("Found at index:", result)  # ➝ 6



# Why is this O(log n) space?

# Each recursive call stores:

#     left, right, mid — passed by value

#     A new function frame (call) on the stack

# The list is halved each time, so the depth of the recursion stack is log₂(n)