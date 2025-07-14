#Scenario 1: Linear scan with scalar vars
#Example: Find the maximum in a list (O(1) space)
def find_max(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val
# Test
numbers = [5, 3, 8, 2, 10, 6]
print("Maximum:", find_max(numbers))  # ➝ 10
# Space Complexity Analysis
#     You're not creating any new lists, arrays, or recursive calls.
#     The only extra memory used is:
#         max_val → a single variable.
#         num → loop variable.
# ➡️ No matter how big arr is (10 items or 10 million), the function uses the same constant amount of space.
#Conclusion
# Space Complexity = O(1)   -Constant Space
# Time Complexity O(n) — Linear scan through arr





# Scenario 2: In-place modification
# Modifying input without extra memory
def reverse_list(arr):
    left, right = 0 , len(arr) -1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr
arr = [5, 3, 8, 2, 10, 6]
print("Reverse List:", reverse_list(arr)) 
#input arr = [5, 3, 8, 2, 10, 6] original
#output  arr = [6, 10, 2, 8, 3, 5] modified
#Space Complexity = O(1) = You're modifying the input array directly, without allocating new memory that grows with input size.





# Scenario 3: Pure Logic / Constant-Time Functions
# Some O(1) functions don't even iterate — they're simple logic.
def is_even(n):
    return n % 2 == 0
print("is_even:", is_even(9))




# Palindrome: A word, phrase, number, or other sequence of characters that reads the same forward and backward.
def is_palindrome(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left +=1
        right -=1
    return True 
arr = [5, 3, 8, 3, 5]
print("is_palindrome:", is_palindrome(arr))
#Space Complexity = O(1)
#  Why is this O(1) in space?
# Let’s break it down:
# What memory is being used?
#     left: a single integer
#     right: another single integer
#     arr: passed by reference, not copied
#     No new arrays, lists, strings, or data structures are created.
# So, regardless of the input size, the memory used is:
#     Exactly 2 variables (left and right) → constant memory



#  Scenario 5: Know when it's not O(1)
def square_all(arr):
    result = []
    for num in arr:
        result.append(num * num)
    return result
arr = [5, 3, 8, 3, 5]
print("square_all:", square_all(arr))
