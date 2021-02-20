#  17.7 COMPUTE THE MAXIMUM WATER TRAPPED BY A PAIR OF VERTICAL LINES

# An array of integers naturally defines a set of Jines parallel to the Y-axis,
# starting from x = 0 as illustrated in Figure 17.4(a) on the next page. The goal
# of this problem is to find the pair of Jines that together with the X-axis
# "trap" the most water. See Figure 17.4(b) on the following page for an example.
# Write a program which takes as input an integer array and returns the pair of
# entries that trap the maximum amount of water.
#
# Hint: Start with 0 and n - 1 and work your way in.

# 11. Container With Most Water

from typing import List

class Solution:
    def get_max_water(self, heights:List[int]) -> int:
        i, j, max_water = 0, len(heights) -1,0

        while i < j:
            width = j - i
            max_water = max(max_water,width * min(heights[i],heights[j]))

            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return max_water

if __name__ == "__main__":
    mySolution = Solution()
    heights = [1,2,1,3,4,4,5,6,2,1,3,1,3,2,1,2,4,1]
    print(mySolution.get_max_water(heights))
