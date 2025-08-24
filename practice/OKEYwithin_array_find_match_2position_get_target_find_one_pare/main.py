# 1. Two Sum (Return Indices)
# 📌 Problem:

# Given a list nums and a target, return the indices of two numbers that add up to the target.
# ❌ Issue:

#     You initially wrote a condition like if nums[i] == nums[j] == target, which checks for both numbers to equal the target, not to add up to it.

#     You also tried return outside a fundfruizcction.

# ✅ Solution:

# Use a function and check the sum of two numbers:

# 🔍 Example:

# nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]


# 1. Brute Force (Nested Loops)
# def two_sum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

# nums = [5,7,3,2]
# target = 9
# print(two_sum(nums,target))

#So, time complexity is O(n²).
#So, space complexity is O(1) — constant space.




# 2. Hash Map (Most Optimal for Unsorted Input)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        # print(f"{i} and {num}")
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
        
nums = [5, 7, 3, 2]
target = 9
print(two_sum(nums, target))  # Output: [0, 2] because 5 + 4 = 9


# Time Complexity: O(n)
# Space Complexity: O(n)

# Constraints:

#     2 <= nums.length <= 10 4
#     -10 9 <= nums[i] <= 10 9
#     -10 9 <= target <= 10 9
#     Only one valid answer exists.


# # 3. Two Pointers (Only Works on Sorted Arrays)
# def two_sum_sorted(nums, target):
#     nums = sorted(nums)
#     left = 0
#     right = len(nums) - 1
#     # print(right)
#     # exit()

#     while left < right:
#         curr_sum = nums[left] + nums[right]
        
#         if curr_sum == target:
#             return [nums[left], nums[right]]
#         elif curr_sum < target:
#             left += 1
#         else:
#             right -= 1

# nums = [2, 7, 5, 8]  # Note: already sorted
# target = 9
# print(two_sum_sorted(nums, target))  # Output: [2, 7]
