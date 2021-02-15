# 16.3 COUNT THE NUMBER OF WAYS TO TRAVERSE A 2D ARRAY
# Write a program that counts how many ways you can go from the top-left to the
# bottom-right in a 2D array.

# Leetcode 62 Unique Paths
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in
#                                                            the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid
# (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?

import math

class Solution:
    # time complexity we iterate over each index once in a 2D MXN array so O(MN)
    # space complexity we store each choice of M and N so O(MN)
    def uniquePaths(self,m:int, n:int)-> int:
        d = [[1] * n for _ in range(m)]

        for col in range(1,m):
            for row in range(1,n):
                # current total = left (d[col - 1][row]) + above (d[col][row - 1])
                d[col][row] = d[col - 1][row] + d[col][row -1]

        return d[m-1][n-1]
    # another solution exists via math solution
    # In other words, we're asked to compute in how many ways one could choose
    # pp elements from p + kp+k elements. In mathematics, that's called binomial
    # coefficients

    # space complexity O(1) nothing stored beyond the calculation
    # Time O((M+N)(log(M+N)loglog(M+N))^2) better than O(k^2)
    def uniquePathsFactorial(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // math.factorial(n - 1) // math.factorial(m - 1)

if __name__ =="__main__":
    mySolution = Solution()
    print(mySolution.uniquePaths(5,5))
    print(mySolution.uniquePathsFactorial(5,5))

    # m col n row
    # [1, 1, 1,  1,  1],
    # [1, 2, 3,  4,  5],
    # [1, 3, 6,  10, 15],
    # [1, 4, 10, 20, 35],
    # [1, 5, 15, 35, 70]]
