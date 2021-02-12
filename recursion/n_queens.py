# 15.3 GENERATE ALL NONATTACKING PLACEMENTS OF n-QUEENS

# Write a program which returns all distinct nonattacking placements of n queens
# on an n x n chessboard, where n is an input to the program.
#
# Hint: If the first queen is placed at (i, j), where can the remaining queens
# definitely not be placed?

# Leetcode 51. N-Queens (Hard)

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def could_place(row, col):
            print("row: ",row," col:",col)
            print(cols[col], " ", hill_diagonals[row-col]," ",dale_diagonals[row + col])
            return not (cols[col] + hill_diagonals[row - col] + dale_diagonals[row + col])

        def place_queen(row, col):
            queens.add((row, col))
            cols[col] = 1
            hill_diagonals[row - col] = 1
            dale_diagonals[row + col] = 1

        def remove_queen(row, col):
            queens.remove((row, col))
            cols[col] = 0
            hill_diagonals[row - col] = 0
            dale_diagonals[row + col] = 0

        def add_solution():
            solution = []
            for _, col in sorted(queens):
                solution.append('.' * col + 'Q' + '.' * (n - col - 1))
            output.append(solution)

        def backtrack(row = 0):
            for col in range(n):
                if could_place(row, col):
                    place_queen(row, col)
                    if row + 1 == n:
                        add_solution()
                    else:
                        backtrack(row + 1)
                    remove_queen(row, col)

        total = 0
        cols = [0] * n
        hill_diagonals = [0] * (2 * n - 1)
        dale_diagonals = [0] * (2 * n - 1)
        queens = set()
        output = []
        backtrack()
        return output

if __name__ =="__main__":
    mySolution = Solution()
    mySolution.solveNQueens(10)
