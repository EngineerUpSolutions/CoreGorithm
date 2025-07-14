# O(log n) – Logarithmic Time
# Divide and conquer (e.g., binary search).

# Imagine you’re playing a guessing game:
# I’m thinking of a number between 1 and 100 — you have to guess it!"

# You could guess like this:
#     Try 1, 2, 3, 4… (That’s O(n), linear time — very slow)



# Smart Guessing Strategy (Divide & Conquer):
    
#     I say:

#     "I'm thinking of a number between 1 and 100. Try to guess it."

# You:

#     Guess 50 — I say "Too low"

#     Guess 75 — I say "Too high"

#     Guess 63 — I say "Too low"

#     Guess 69 — I say "Correct!"

# You cut the range in half every time.
# You only needed 4 guesses instead of 100!

#That’s logarithmic time: each step halves the problem


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    # print(right)
    # print(arr)
    # exit()

    while left <= right:
        mid = (left + right) // 2
        #print(f"Guessing index {mid}, value {arr[mid]}")
        if arr[mid] == target:
            print("Found it!")
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    print("Not found")
    return -1

# Sorted list to search in
arr = list(range(1, 11))  # [1, 2, 3, ..., 100]
binary_search(arr, 50)
