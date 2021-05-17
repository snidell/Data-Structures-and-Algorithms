import heapq
import math
from typing import List


class Solution:
    def min_effort(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        # where i visisted
        visited = [[False] * cols for _ in range(rows)]
        # difference matrix
        differences = [[math.inf] * cols for _ in range(rows)]
        # track difference,x,y coordinate in a tuple
        # store tuple in a min heap
        heap = [(0,0,0)]
        differences[0][0] = 0
        while heap:
            difference,row,col = heapq.heappop(heap)
            visited[row][col] = True
            # loop through heap and do BFS
            for drow,dcol in [[0,1],[1,0],[0,-1],[-1,0]]:
                adjacent_row = row + drow
                adjacent_col = col + dcol
                if 0<= adjacent_row < rows and  0 <= adjacent_col < cols and not visited[adjacent_row][adjacent_col]:
                    # find min difference between x,y coordinate
                    current_difference = abs(heights[adjacent_row][adjacent_col]-heights[row][col])
                    max_difference = max(current_difference,differences[row][col])

                    if differences[adjacent_row][adjacent_col] > max_difference:
                        differences[adjacent_row][adjacent_col] = max_difference
                        heapq.heappush(heap,(max_difference,adjacent_row,adjacent_col))

        # exit loop and return the value at [-1][-1]
        print(differences)
        return differences[-1][-1]




if __name__ == "__main__":
    mySolution = Solution()
    heights=[
                [1, 2, 2],
                [3, 8, 2],
                [5, 3, 5]
              ]
    print(mySolution.min_effort(heights))
