# Function: Return All Even Numbers (O(n) Space)

def get_even_numbers(arr):
    result = []
    for num in arr:
        if num % 2 == 0:
            result.append(num)
    return result

# Test
arr = [1, 2, 3, 4, 5, 6]
print("Even numbers:", get_even_numbers(arr))  # ➝ [2, 4, 6]


# Why is this O(n) Space?

#     We are creating a new list result to store the even numbers.

#     In the worst case (e.g. if all numbers are even), result will have n elements.

# ➡️ Space grows linearly with the size of the input list ⇒ O(n)