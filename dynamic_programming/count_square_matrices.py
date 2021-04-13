from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = []
        for i in range(m):
            dp.append([0] * n)
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j],dp[i][j -1],dp[i - 1][j - 1]) +1
                else:
                    dp[i][j] = 0

        total = 0

        for i in range(len(dp)):
            print(dp[i])
            total = total + sum(dp[i])
        return total


if __name__ =="__main__":
    mySolution = Solution()
    matrix =[
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
    print(mySolution.countSquares(matrix))
