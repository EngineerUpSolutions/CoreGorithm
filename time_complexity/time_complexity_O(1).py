# Scenario 1:
# Direct Access / Indexing 
# No matter the size of the input, it runs in the same time.
def get_first_element(arr):
    return arr[0]
# Test
print("get_first_element",get_first_element([10, 20, 30, 40]))  # ➝ 10
# It always accesses the first element. Doesn't matter if the list has 10 or 10,000 elements.



# Scenario 2: Simple Arithmetic / Logic
def is_even(n):
    return n % 2 == 0
print("is_even",is_even(10)) 
# Why it's O(1):
#     %, ==, and return are all constant-time operations.
#     No loops, no recursion.
#  ❌ Trap to Avoid:
#      def count_even(numbers):
#     count = 0
#     for n in numbers:
#         if n % 2 == 0:
#             count += 1
#     return count
# ❌ This is O(n) — because it loops through the input.


# Scenario 3: Return Constant
def get_pi():
    return 3.14159
print("get_pi",get_pi()) 




#Scenario 4: Set / Dictionary Lookup
def is_registered(user_id, registered_ids):
    return user_id in registered_ids  # Assume registered_ids is a set
registered_ids = {100, 200, 300, 400, 500}
user_id=100
print("Is user registered?", is_registered(user_id, registered_ids))  
# Why it's O(1) (on average):

#     Python set and dict use hash tables.

#     Average-case insert / lookup / delete = O(1).

#     Worst-case is O(n), but rare and usually ignored unless stated.



# Scenario 5: Variable Assignment / Swap
def swap(a, b):
    a, b = b, a
    return a, b
a, b = 1,2
print("swap", swap(a,b))  
# Why it's O(1):

#     Only a fixed number of operations, regardless of values.

# Used a lot in sorting algorithms (e.g., quicksort partition step)




# 🔹 Scenario 6: Bit Manipulation
def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0
n =32
print("is_power_of_two", is_power_of_two(n))  
# Why it's O(1):

#     Bitwise & is constant-time for fixed-size integers (32 or 64 bits).

#     Always runs in the same number of CPU instructions.

# ✅ Interview Use Case:

# Power-of-two checks, optimization, low-level systems.
