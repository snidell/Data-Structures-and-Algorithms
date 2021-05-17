# 1428. Leftmost Column with at Least a One
# (This problem is an interactive problem.)
#
# A row-sorted binary matrix means that all elements are 0 or 1 and each row of
# the matrix is sorted in non-decreasing order.
#
# Given a row-sorted binary matrix binaryMatrix, return the index (0-indexed) of
# the leftmost column with a 1 in it. If such an index does not exist, return -1.
#
# You can't access the Binary Matrix directly. You may only access the matrix
# using a BinaryMatrix interface:
#
# BinaryMatrix.get(row, col) returns the element of the matrix at index (row, col)
#  (0-indexed).
# BinaryMatrix.dimensions() returns the dimensions of the matrix as a list of 2
# elements [rows, cols], which means the matrix is rows x cols.
# Submissions making more than 1000 calls to BinaryMatrix.get will be judged
# Wrong Answer. Also, any solutions that attempt to circumvent the judge will
# result in disqualification.
#
# For custom testing purposes, the input will be the entire binary matrix mat.
# You will not have access to the binary matrix directly.

from typing import List

class BinaryMatrix():
    def __init__(self,matrix:List[List[int]]):
        self.matrix = matrix
    def get(self,row:int,col:int)->int:
        return self.matrix[row][col]
    def dimensions(self) ->List[int]:
        return [len(self.matrix),len(self.matrix[0])]

class Solution:
    def leftMostColumWithOne(self,binaryMatrix:'BinaryMatrix')-> int:
        rows,cols = binaryMatrix.dimensions()

        # set point to top right
        current_row = 0
        current_col = cols -1

        while current_row < rows and current_col >= 0:
            # we are looking for the 1 to zero transition here
            if binaryMatrix.get(current_row,current_col) == 0:
                # move pointer down a row
                current_row += 1
            else:
                # move the pointer left
                current_col -= 1
        # if we never left the last column, it must have been all 0's
        return current_col + 1 if current_col != cols -1 else -1

if __name__ =="__main__":
    matrix = [[0,0,0,1],[0,0,1,1],[0,0,0,0]]
    myBinaMatrix = BinaryMatrix(matrix)
    mySolution = Solution()
    print(mySolution.leftMostColumWithOne(myBinaMatrix))
