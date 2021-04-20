# Leetcode 562. Longest Line of Consecutive One in Matrix
# Given a 01 matrix M, find the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal or anti-diagonal.
#
# Example:
# Input:
# [[0,1,1,0],
#  [0,1,1,0],
#  [0,0,0,1]]
# Output: 3

from typing import List

class Solution:
    def longestLine(self, M: List[List[int]]) -> int:
        if not M:
            return 0
        rows,cols = len(M),len(M[0])
        visited = [[False]*cols for i in range(rows)]

        def dfs(grid,row,col,visited,direction):
            if not(row>=0 and col >= 0 and row <rows and col < cols and grid[row][col] == 1 and visited[row][col] == False):
                return 0
            visited[row][col] = True

            recursion = 0

            if direction == "horizontal":
                recursion += dfs(grid,row - 1,col,visited,direction)
                recursion += dfs(grid,row + 1,col,visited,direction)
            elif direction == "vertical":
                recursion += dfs(grid,row,col - 1,visited,direction)
                recursion += dfs(grid,row,col + 1,visited,direction)
            elif direction == "diagonal":
                recursion += dfs(grid,row -1,col - 1,visited,direction)
                recursion += dfs(grid,row + 1,col + 1,visited,direction)
            elif direction == "anti-diagonal":
                recursion += dfs(grid,row + 1,col - 1,visited,direction)
                recursion += dfs(grid,row - 1,col + 1,visited,direction)
            visited[row][col] = False

            return 1 + recursion

        result = 0

        # loop through the matrix
        for row in range(rows):
            for col in range(cols):
                # find a 1
                if M[row][col] == 1:
                    # then check left/right ie horizontal
                    horizontal = dfs(M,row,col,visited,"horizontal")
                    # check up down
                    vertical = dfs(M,row,col,visited,"vertical")
                    # check diagonal
                    diagonal = dfs(M,row,col,visited,"diagonal")
                    # check anti-diagonal
                    anti_diagonal = dfs(M,row,col,visited,"anti-diagonal")
                    result = max(result,horizontal,vertical,diagonal,anti_diagonal)
        return result


    def longestLineDP(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        if len(M) == 0:
            return 0

        # 3d matrix that stores the maxmial choices of each direction
        dp = [[ [0, 0, 0, 0] for j in range(len(M[0]))] for i in range(len(M))]
        max_len = 0
        for row in range(len(M)):
            for col in range(len(M[0])):
                if M[row][col] == 1:
                    # check vertical
                    dp[row][col][0] = dp[row][col-1][0] + 1 if col > 0 else 1
                    # check horizontal
                    dp[row][col][1] = dp[row-1][col][1] + 1 if row > 0 else 1
                    # check diagonal
                    dp[row][col][2] = dp[row-1][col-1][2] + 1 if row > 0 and col > 0 else 1
                    # check anti diagonal
                    dp[row][col][3] = dp[row-1][col+1][3] + 1 if row > 0 and col < len(M[0])-1 else 1

                max_len = max(max_len, dp[row][col][0], dp[row][col][1], dp[row][col][2], dp[row][col][3])
        print(dp)
        return max_len



if __name__ =="__main__":
    mySolution = Solution()
    matrix = [[0,1,1,0],
              [0,1,1,0],
              [0,0,0,1]
             ]
    # print(mySolution.longestLine(matrix))
    print(mySolution.longestLineDP(matrix))
