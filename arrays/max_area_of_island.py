# Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's
# (representing land) connected 4-directionally (horizontal or vertical.) You
# may assume all four edges of the grid are surrounded by water.
#
# Find the maximum area of an island in the given 2D array. (If there is no
# island, the maximum area is 0.)
# Example 1:
#
# [[0,0,1,0,0,0,0,1,0,0,0,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,1,1,0,1,0,0,0,0,0,0,0,0],
#  [0,1,0,0,1,1,0,0,1,0,1,0,0],
#  [0,1,0,0,1,1,0,0,1,1,1,0,0],
#  [0,0,0,0,0,0,0,0,0,0,1,0,0],
#  [0,0,0,0,0,0,0,1,1,1,0,0,0],
#  [0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Given the above grid, return 6. Note the answer is not 11, because the island
# must be connected 4-directionally.
# Example 2:
#
# [[0,0,0,0,0,0,0,0]]

from typing import List

class Solution:
    def maxAreaOfIsland(self,grid :[List[int]])->int:
        def findArea(grid,row,col)->int:
            # lets stay in bounds. and check if its a 1. if not return zero
            if not(row>= 0 and row < rows and col>=0 and col< cols and grid[row][col] !=0):
                return 0
            # if we have been this far. We dont want to recurse on this island
            # seciton again so mark it a zero so we dont create a cycle
            grid[row][col] = 0
            left = findArea(grid,row-1,col)
            right = findArea(grid,row + 1, col)
            down = findArea(grid,row,col - 1)
            up = findArea(grid,row,col + 1)

            # if we get here we know 1.) we are in the grid and 2.) its a 1
            return left+right+up+down+1

        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0

        for row in range(rows-1):
            for col in range(cols-1):
                # if we have a one in this slot then see if they're are more conencted 1s
                if grid[row][col]==1:
                    currentArea = findArea(grid,row,col)
                    maxArea = max(maxArea,currentArea)

        return maxArea




if __name__ =="__main__":
    mySolution = Solution()
    myIslands =[[0,0,1,0,0,0,0,1,0,0,0,0,0],
                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                 [0,1,1,0,1,0,0,0,0,0,0,0,0],
                 [0,1,0,0,1,1,0,0,1,0,1,0,0],
                 [0,1,0,0,1,1,0,0,1,1,1,0,0],
                 [0,0,0,0,0,0,0,0,0,0,1,0,0],
                 [0,0,0,0,0,0,0,1,1,1,0,0,0],
                 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(mySolution.maxAreaOfIsland(myIslands))
