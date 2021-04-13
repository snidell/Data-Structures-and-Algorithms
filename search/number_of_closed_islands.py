# 1254. Number of Closed Islands
# Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal
# 4-directionally connected group of 0s and a closed island is an island totally
# (all left, top, right, bottom) surrounded by 1s.
#
# Return the number of closed islands.

from typing import List
class Solution:
    def closedIslands(self,grid:List[List[int]])->int:
        # need a grid to do anything
        if not grid:
            return 0
        rows, cols = len(grid),len(grid[0])
        LAND = 0
        WATER = 1
        result = 0
        # search along permiter for any Land and switch it to water as
        # these are invalid numbers
        def dfs(grid,row,col):
            if not(row>=0 and col>=0 and col<cols and row <rows and grid[row][col] == LAND):
                return
            # flip this to water so we dont count it again
            grid[row][col] = WATER

            dfs(grid,row - 1,col)
            dfs(grid,row + 1,col)
            dfs(grid,row,col - 1)
            dfs(grid,row,col + 1)
            return
        # top row bottom row
        for row in [0,rows-1]:
            for col in range(cols):
                print(row,col)
                if grid[row][col] == LAND:
                    dfs(grid,row,col)
        for row in range(rows):
            for col in [0,cols-1]:
                if grid[row][col] == LAND:
                    dfs(grid,row,col)

        for row in range(1,rows):
            for col in range(1,cols):
                if grid[row][col] == LAND:
                    result += 1
                    dfs(grid,row,col)        

        return result


        # search rest of the table from 1,1 if we find land do a DFS on the item and change those items to water

        # return the result. this is 2*O(n^2)

if __name__ =="__main__":
    mySolution = Solution()
    grid = [
            [1,1,1,1,1,1,1,0],
            [1,0,0,0,0,1,1,0],
            [1,0,1,0,1,1,1,0],
            [1,0,0,0,0,1,0,1],
            [1,1,1,1,1,1,1,0]
           ]
    print(mySolution.closedIslands(grid))
