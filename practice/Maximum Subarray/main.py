# Dynamic Programming / Sliding Window Pattern

# “If I add this number to my current sum, will it get better, or worse?”
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum= nums[0]
        max_sum= nums[0]
        print(f"current_sum = {current_sum}, max_sum = {max_sum}")
        for i in range(1,len(nums)):
            print(i)

        # for num in range(nums):
        #     print(num)
        # return
    
    
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [3, -2, 5, -1]
# Create object and call method
s = Solution()
print("Final result:", s.maxSubArray(nums))


# Constraints:

#     1 <= nums.length <= 105
#     -104 <= nums[i] <= 104


# What’s the challenge?

# The hard part is:

#     You don’t know where the subarray starts or ends.

#     You don’t know how long it is.

#     You can’t just test all combinations — too slow (would be O(n²) or worse).

# Instead, you want to figure out:

#     How can I explore the array in one pass and still find the best subarray sum?






# from typing import List

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         current_sum = nums[0]
#         max_sum = nums[0]
#         print(f"Start: current_sum = {current_sum}, max_sum = {max_sum}")

#         for i in range(1, len(nums)):
#             num = nums[i]
#             current_sum = max(num, current_sum + num)
#             max_sum = max(max_sum, current_sum)
#             print(f"Step {i}: num = {num}, current_sum = {current_sum}, max_sum = {max_sum}")

#         return max_sum

# # Test input
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# # Create object and call method
# s = Solution()
# print("Final result:", s.maxSubArray(nums))
