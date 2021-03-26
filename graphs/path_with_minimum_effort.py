# Leetcode 1631. Path With Minimum Effort
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D
# array of size rows x columns, where heights[row][col] represents the height of
# cell (row, col). You are situated in the top-left cell, (0, 0), and you hope to
# travel to the bottom-right cell, (rows-1, columns-1) (i.e., 0-indexed). You can
# move up, down, left, or right, and you wish to find a route that requires the
# minimum effort.
#
# A route's effort is the maximum absolute difference in heights between two
# consecutive cells of the route.
#
# Return the minimum effort required to travel from the top-left cell to the
# bottom-right cell.

from typing import List
import math
import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row = len(heights)
        col = len(heights[0])
        # intialize difference matrix. this tells us the current distance it takes to get to each cell
        difference_matrix = [[math.inf]*col for _ in range(row)]
        # first cell is zero as its the starting point
        difference_matrix[0][0] = 0
        # visited matrixs prevents us from cycling back to cells we already have visited
        visited = [[False]*col for _ in range(row)]
        # construct queue for BFS. maybe use a class for cleanliness
        queue = [(0, 0, 0)]  # difference, x, y
        while queue:
            difference, x, y = heapq.heappop(queue)
            visited[x][y] = True
            # loop through the directions right, up left, down
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                adjacent_x = x + dx
                adjacent_y = y + dy
                # lets stay in bounds and not go back to cells we touched before
                if 0 <= adjacent_x < row and 0 <= adjacent_y < col and not visited[
                        adjacent_x][adjacent_y]:
                    # when i move to the next cell from this cell what is the effort ?
                    current_difference = abs(
                        heights[adjacent_x][adjacent_y]-heights[x][y])
                    # we are looking at the smallest effort along the path therefore we need to take the max of the two
                    max_difference = max(
                        current_difference, difference_matrix[x][y])
                    # update the difference matrix with the max if its bigger
                    if difference_matrix[adjacent_x][adjacent_y] > max_difference:
                        difference_matrix[adjacent_x][adjacent_y] = max_difference
                        # optmization if we add to the queue in this if statement we know that we have pushed the smallest for the current xy
                        # this will still work outside of the if like a normal BFS however TLE will be encountered
                        heapq.heappush(
                            queue, (max_difference, adjacent_x, adjacent_y))

        return difference_matrix[-1][-1]

if __name__ =="__main__":
    mySolution = Solution()
    matrix = [[1,2,2],[3,8,2],[5,3,5]]
    print(mySolution.minimumEffortPath(matrix)) # return 2
    # difference matrixs# [
    #     [0, 1, 1],
    #     [2, 5, 1],
    #     [2, 2, 2]]
