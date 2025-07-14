# Function: Merge Sort — O(n log n) Time and O(n) or O(n log n) Space (depends on implementation)

# We'll show a version that allocates new sublists at each recursion level — which can lead to O(n log n) space in total.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # slice → new list
    right = merge_sort(arr[mid:])  # slice → new list
    
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

# Test
arr = [9, 5, 2, 8, 1, 6]
print("Sorted:", merge_sort(arr))  # ➝ [1, 2, 5, 6, 8, 9]


# Why is this O(n log n) Space?

#     At each recursion level, you're creating new sublists via slicing: arr[:mid], arr[mid:]

#     You have log n recursive levels

#     At each level, up to n elements worth of slices are created

#     Total auxiliary memory across all levels = O(n log n)



