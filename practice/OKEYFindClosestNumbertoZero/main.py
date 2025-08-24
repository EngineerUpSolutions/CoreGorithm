from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        best = nums[0]
        for k in range(1,len(nums)):
            x = nums[k]  # first candidate for the closest to 0
            
            #absolute manually
            abs_x = -x if x < 0 else x
            abs_best = -best if best < 0 else best
            
            #pick the one with smaller absolute value
            #pick if there is tie, the largest one
            
            if abs_x < abs_best or (abs_x == abs_best and x > best):
                best = x
        return best
                
s = Solution()
nums = [-4,-2,1,4,8]
s = Solution()
print(s.findClosestNumber(nums))