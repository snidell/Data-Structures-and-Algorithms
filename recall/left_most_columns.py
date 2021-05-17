
from typing import List

class BinaryMatrix():
    def __init__(self,matrix:List[List[int]]):
        self.matrix = matrix
    def get(self,row:int,col:int)->int:
        return self.matrix[row][col]
    def dimensions(self) ->List[int]:
        return [len(self.matrix),len(self.matrix[0])]

class Solution:
    def left_most_column(self,matrix:"binaryMatrix")-> int:
        rows, cols = matrix.dimensions()
        row, col = 0, cols-1
        result = float('inf')
        while row < rows and col >=0:
            if matrix.get(row,col) == 1:
                col -= 1
            else:
                row += 1

        return -1 if col == cols-1 else col+1


if __name__ =="__main__":
    mySolution = Solution()

    matrix = [[0,0,0,1],[0,0,1,1],[0,0,0,0]]
    myBinaMatrix = BinaryMatrix(matrix)

    print(mySolution.left_most_column(myBinaMatrix))
