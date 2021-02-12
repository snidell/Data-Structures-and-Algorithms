# 15.10 Soduku solver
# Leetcode 37
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes
# of the grid.
# The '.' character indicates empty cells.

# Back tracking blue print:
# https://www.youtube.com/watch?v=Zq4upTEaQyM&list=PLiQ766zSC5jM2OKVr8sooOuGgZkvnOCTI&index=1

# Three keys to back tracking:
# 1.) Choices - core choice of each step. Build cells by making choices
# cell sits in a row and column. Place an item is making a choice
# 2.) Constraints - Did the item i place break the row or column? if this is
# valid placement recurse on this decision to reach out base case
# 3.) Goal base case  is out of bounds on the row. final base case is out of
# bounds on the final row
# What happens if its a bad decision ? undone the decision return to original state
# How to identify backtracking problems ? look for questions that are exhuastive
# in nature. "Compute all", "Generate all"
# backtracking is often huge space/time complxity O(N!)+


from typing import List
from collections import defaultdict
class Solution:
    def solveSudoku(self,board: List[List[int]])-> None:
        # check if the current number can be placed in the current row
        # col or cell
        def could_place(d, row, col):
            return not (d in rows[row] or d in columns[col] or d in boxes[box_index(row,col)])

        # place number d in (row,col) cell
        def place_number(d,row,col):
            rows[row][d] += 1
            columns[col][d] += 1
            boxes[box_index(row,col)][d] += 1
            board[row][col] = str(d)

        # remove number d in (row,col) cell
        def remove_number(d,row,col):
            del rows[row][d]
            del columns[col][d]
            del boxes[box_index(row,col)][d]
            board[row][col] = '.'

        # call backtrack function in recursion to continue to place numbers
        # till the moment we have a solution
        def place_next_numbers(row,col):
            # if we are in the last cell we have a solution
            if col == N - 1 and row == N -1:
                nonlocal sudoku_solved
                sudoku_solved = True
            # if not yet solved
            else:
                # if we are at the end of the row go to next row
                if col == N-1:
                    backtrack(row + 1,0)
                # go to next column
                else:
                    backtrack(row,col + 1)

        def backtrack(row = 0, col = 0):
            if board[row][col] == '.':
                # iterate over all numbers 1-9
                for d in range(1,10):
                    if could_place(d,row,col):
                        place_number(d,row,col)
                        place_next_numbers(row,col)
                        # if solved there is no need to backtrack
                        # since the single unique solution is is promised
                        if not sudoku_solved:
                            remove_number(d,row,col)
            else:
                place_next_numbers(row,col)
        # box size
        n = 3
        # row size
        N = n * n
        # function to compute box index
        box_index = lambda row,col: (row//n) * n  + col//n

        # initialize rows
        rows = [defaultdict(int)for i in range(N)]
        columns = [defaultdict(int) for i in range(N)]
        boxes = [defaultdict(int) for i in range(N)]
        print(rows)
        for i in range(N):
            for j in range(N):
                if board[i][j] != '.':
                    d = int(board[i][j])
                    place_number(d,i,j)
        sudoku_solved = False
        backtrack()
        print(rows)


if __name__ =="__main__":
    mySolution = Solution()
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]
    mySolution.solveSudoku(board)
    print(board)
