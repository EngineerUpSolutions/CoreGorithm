from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j=(0,len(height)-1)
        [print(j)]
        # max_area = 0

        # while i<j:
        #     width = j - i
        #     h = min(height[i],height[j])
        #     area = width * h
        #     max_area= max(max_area,area)
            


        #     if i<j:
        #         i +=1
        #         j -=1
        # return max_area

        



height= [1,2,3,4,5,6,7,8,9]
s = Solution()
print(s.maxArea(height))


# Constraints:

#     n == height.length
#     2 <= n <= 105
#     0 <= height[i] <= 104


# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

