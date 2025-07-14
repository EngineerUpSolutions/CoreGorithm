🟥🟩🟦 

🟩 Time Complexity
-It describes how the runtime of an algorithm increases as the size of the input increases.
-It's measured using Big O notation (e.g, O(1), O(n), O(n²))
-It answers: "if the input gets bigger, how much slower will this get?"

NOTATION         MEANING             EXAMPLE
O(1)             Constant time       Accessing an element in an array
O(n)             Linear time         Looping through a list once
O(n²)            Quadratic time      Nested loops
O(log n)         Logarithmic time    Binary search
O(n log n)       Log-linear time     Merge sort, Quick sort(avg)

example:  
def print_all(nums):
    for num in nums:                  //Here, the algorithm runs n times → Time Complexity: O(n)
        print(num)


🟩 Space Complexity
-It describes how much memory the algorithn needs relative to the input size
-It includes variables, data structures, function call stack, etc..


example
def make_copy(nums):
    new_list = []
    for num in nums:
        new_list.append(num)          //You're using extra memory to store new_list, which is proportional to the input → Space Complexity: O(n)
    return new_list



🟦 Summary Table
| Aspect           | Time Complexity         | Space Complexity        |
| ---------------- | ----------------------- | ----------------------- |
| What it measures | Runtime growth          | Memory growth           |
| Key notation     | Big O (`O(n)`, etc.)    | Big O (`O(1)`, `O(n)`)  |
| Affected by      | Loops, recursion, calls | Variables, data storage |
