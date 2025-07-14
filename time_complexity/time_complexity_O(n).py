# Scenario 1: Simple Iteration over Input
#     One operation per element — linear pass.
# Time grows proportionally with input size.
def print_all_elements(arr):
    for num in arr:
        print(num)
    return "okey"
# Test
print("print_all_elements",print_all_elements([1, 2, 3, 4, 5]))
#If the list has 5 elements → 5 prints. If it has 1,000 → 1,000 prints.
# Conclusion:
# Factor	Value
# Input size	n
# Number of operations	n (one per item)
# Time Complexity	O(n)
# The function performs a linear pass through the list — that's the definition of O(n) time.


# Scenario 2: Accumulation (e.g. sum, max, min)
#     One pass to compute a single value from input.
#     Common in problems like: total sum, maximum, minimum, average, etc.
def find_sum(arr):
    total = 0
    for num in arr:
        total += num
    return total
# Test
print("find_sum:", find_sum([1, 2, 3, 4, 5]))  # ➝ 15
# Explanation:
# The function visits each element once and performs one addition per item.
# So if the array has n elements, it does n additions.

# Conclusion:
# Factor               | Value
#----------------------|---------------------
# Input size           | n
# Number of operations | n additions
# Time Complexity      | O(n)






# Scenario 3: Linear Search
#     One pass to find a specific element (target).
#     Stops early if found, but in worst case scans the full list.

def find_target(arr, target):
    for num in arr:
        if num == target:
            return True
    return False
# Test
print("find_target:", find_target([1, 3, 5, 7, 9], 7))  # ➝ True
# Explanation:
# In the worst case, the function must check every element.
# So even if it returns early sometimes, we count the worst case in Big-O.

# Conclusion:
# Factor               | Value
#----------------------|---------------------
# Input size           | n
# Number of comparisons| up to n
# Time Complexity      | O(n)




# Scenario 4: Copy / Transform (Map)
#     One pass to create a new list by transforming each element.

def square_elements(arr):
    result = []
    for num in arr:
        result.append(num *num)
    return result
# Test
print("square_elements:", square_elements([1, 2, 3, 4]))  # ➝ [1, 4, 9, 16]
# Explanation:
# The function loops through the entire input list once.
# For each element, it computes the square and appends it to a new list.
# So the number of operations grows linearly with the input.

# Conclusion:
# Factor               | Value
#----------------------|---------------------
# Input size           | n
# Number of operations | n (one per element)
# Time Complexity      | O(n)
