# Objective:

# Implement the merge sort algorithm and use it to sort a list of random integers. Explain how the algorithm achieves O(n log n) time complexity.


import random

# Merge Sort Algorithm
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Divide
    right = merge_sort(arr[mid:])  # Divide

    return merge(left, right)      # Conquer

def merge(left, right):
    sorted_arr = []
    i = j = 0

    # Merge the two halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    # Append any remaining elements
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

# Demo
if __name__ == "__main__":
    arr = [random.randint(1, 100) for _ in range(10)]
    print("Unsorted:", arr)
    sorted_arr = merge_sort(arr)
    print("Sorted:  ", sorted_arr)
