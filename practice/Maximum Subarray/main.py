from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum={}
        max_sum={}
        for num in range(nums):
            print(num)
        return
    
    
# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [3, -2, 5, -1]


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
