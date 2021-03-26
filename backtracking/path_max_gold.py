from typing import List

class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def find_gold(grid,row,col,visited):
            # stay in bounds, dont back cycle no need to visit zeros

            # if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or check[i][j] or grid[i][j] == 0:
            if row < 0 or col < 0 or col >= cols or row >= rows:
                return 0
            print(row,rows,col,cols)
            if visited[row][col] or grid[row][col] == 0:
                return 0
            visited[row][col] = True
            left = find_gold(grid,row,col - 1,visited)
            right = find_gold(grid,row,col + 1,visited)
            up = find_gold(grid,row - 1,col,visited)
            down = find_gold(grid,row + 1,col,visited)
            # we need to set this back to False for back tracking. Once we have
            # ran through this path we need to be able to search it again and
            # comapre totals of a new path
            visited[row][col] = False

            return max(left,right,up,down) + grid[row][col]

        gold_max = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    current_gold = find_gold(grid,row,col,visited)
                    gold_max = max(gold_max,current_gold)
        return gold_max



if __name__ =="__main__":
    mySolution = Solution()
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
    print(mySolution.getMaximumGold(grid))
