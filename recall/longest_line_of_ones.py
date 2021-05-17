from typing import List

class Solution:
    # space is the dp matrix O(N^3)
    
    def longest_line(self,matrix:List[List[int]]) -> int:
        # get rows/columns
        rows = len(matrix)
        cols = len(matrix[0])
        # initialize 2d matrix (0,0,0,0) up/down, left/right, diagonal, anti-diagonal
        dp = [[[0,0,0,0]]* cols for _ in range(rows)]
        max_length = 0
        # loop through the matrix
        for row in range(rows):
            for col in range(cols):
                # check left
                if matrix[row][col] == 1:
                    # go each directions. choose to pick if one then pick else 1
                    # check vertical
                    dp[row][col][0] = dp[row][col - 1][0] + 1 if col > 0 else 1
                    # check horizontal
                    dp[row][col][1] = dp[row - 1][col][1] + 1 if row > 0 else 1
                    # check diagonal
                    dp[row][col][2] = dp[row - 1][col - 1][2] + 1 if row > 0 and col > 0 else 1
                    # check antidagonal
                    dp[row][col][3] = dp[row - 1][col + 1][3] + 1 if row > 0 and col < cols-1 else 1
                    max_length = max(dp[row][col][0],dp[row][col][1],dp[row][col][2],dp[row][col][3])

        # once we have each direction calculated we take the max of all directions and match against result max
        # return result max
        return max_length



if __name__ =="__main__":
    mySolution = Solution()
    matrix = [[0,1,1,0],[0,1,1,0],[0,0,0,1]]
    print(mySolution.longest_line(matrix))
