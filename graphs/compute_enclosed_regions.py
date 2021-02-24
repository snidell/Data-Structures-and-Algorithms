# 18.3 COMPUTE ENCLOSED REGIONS

# Let A be a 20 array whose entries are either W or B. Write a program that takes
# A, and replaces all Ws that cannot reach the boundary with a B.
#
# Hint: It is easier to compute the complement of the desired result.
#
# The book has a poor explaination and poor un clear code so we will use the
# leetcode explaination and code instead

# Leetcode 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/
# Given an m x n matrix board containing 'X' and 'O', capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
#
# Explanation: Surrounded regions should not be on the border, which means that
# any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not
# on the border and it is not connected to an 'O' on the border will be flipped
# to 'X'. Two cells are connected if they are adjacent cells connected
# horizontally or vertically.

from itertools import product
from collections import deque
from typing import List
class Solution:
    def solve(self,board:List[List[str]]) -> None:
        # change board in place no need to return

        # we need a 2d board else exit
        if not board or not board[0]:
            return
        self.ROWS = len(board)
        self.COLS = len(board[0])

        # get all board cells
        borders = list(product(range(self.ROWS),[0,self.COLS-1]))\
                + list(product([0,self.ROWS - 1],range(self.COLS)))

        # mark the escaped cells with a placeholder eg 'E'
        for row,col in borders:
            # self.DFS(board,row,col)
            self.BFS(board,row,col)
        # flip the captured rows ('O'->'X') and the escaped one ('E'->'O')
        for r in range(self.ROWS):
            for c in range(self.COLS):
                if board[r][c] == 'O': board[r][c] ='X' # captured
                if board[r][c] == 'E': board[r][c] = 'O' # escaped

    # time complexity O(N) worst case it contains only o cells
    # space complexity O(N)  list of border cells and O(N) and depth of the
    # worst recursive call is O(N)
    def BFS(self, board, row, col):
            from collections import deque
            queue = deque([(row, col)])
            while queue:
                (row, col) = queue.popleft()
                if board[row][col] != 'O':
                    continue
                # mark this cell as escaped
                board[row][col] = 'E'
                # check its neighbor cells
                if col < self.COLS-1: queue.append((row, col+1))
                if row < self.ROWS-1: queue.append((row+1, col))
                if col > 0: queue.append((row, col-1))
                if row > 0: queue.append((row-1, col))

    # Time complexity O(N)
    # space complexity O(N)
    def DFS(self, board, row, col):
        from collections import deque
        stack = deque([(row, col)])
        while stack:
            # pop out the _tail_ element, rather than the head.
            (row, col) = stack.pop()
            if board[row][col] != 'O':
                continue
            # mark this cell as escaped
            board[row][col] = 'E'
            # check its neighbour cells
            if col < self.COLS-1: stack.append((row, col+1))
            if row < self.ROWS-1: stack.append((row+1, col))
            if col > 0: stack.append((row, col-1))
            if row > 0: stack.append((row-1, col))

if __name__ =="__main__":
    mySolution = Solution()
    board = [["X","X","X","X"],
             ["X","X","O","X"],
             ["X","O","X","X"],
             ["X","O","X","X"]]
    mySolution.solve(board)
    print(board)
    # [['X', 'X', 'X', 'X'],
    # ['X', 'X', 'X', 'X'],
    # ['X', 'O', 'X', 'X'],
    # ['X', 'O', 'X', 'X']]
