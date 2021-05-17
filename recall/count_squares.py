
from typing import List

class Solution:
    def count_squares(self,matrix: List[List[int]])-> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                # if its a one we need to look up back and up/back and add a 1 to it
                if matrix[row][col] == 1:
                    # since we are looking back we need ot make sure we dont go out of bounds here
                    if row >= 1 and col >= 1:
                        dp[row][col] = 1 + min(dp[row -1][col],dp[row][col-1],dp[row-1][col-1])
                    else:
                        dp[row][col] = 1
        total = 0
        for row in range(rows):
            print(dp[row])
            total += sum(dp[row])
        return total





if __name__ =="__main__":
    mySolution = Solution()
    matrix = [
              [0,1,1,1],
              [1,1,1,1],
              [0,1,1,1]
            ]
    print(mySolution.count_squares(matrix))
