# 17.8 COMPUTE THE LARGEST RECTANGLE UNDER THE SKYLINE


# You are given a sequence of adjacent buildings. Each has unit width and an
# integer height. These buildings form the skyline of a city. An architect wants
# to know the area of a largest rectangle contained in this skyline.

# Leetcode 84. Largest Rectangle in Histogram (hard)

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        # values that are left in the stack need to be evaluated
        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)
        return max_area


if __name__ == "__main__":
     mySolution = Solution()
     heights = [6,7,5,2,4,5,8,3]
     heights2 = [6,7,5,2,4,5,8,9,10,11,10,9,12]
     print(mySolution.largestRectangleArea(heights2))
