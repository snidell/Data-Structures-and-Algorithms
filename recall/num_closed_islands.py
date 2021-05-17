
from typing import List

class Solution:
    def closed_islands(self,grid: List[List[int]]) ->int:
        # closed island does not touch the edges
        # so we need to turn those in "water" by finding them and using DFS
        # then use DFS to find the rest of the islands
        rows = len(grid)
        cols = len(grid[0])
        LAND = 0
        WATER = 1

        def dfs(row,col,grid):
            if not row >= 0 and row <rows and col >= 0 and col <cols and grid[row][col] == LAND:
                return

         # loop through the top and bottom of the grid and remove all that are land
         for row in [0,len(rows)-1]:
             for col in range(cols):
                 if grid[row][col] == LAND:
                     dfs()
