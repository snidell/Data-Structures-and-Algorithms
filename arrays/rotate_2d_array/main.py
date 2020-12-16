# 5.19 ROTATE A 2D ARRAY
from typing import List
class Solution:
    # roates clockwise O(n^2) time and O(1) space
    def rotate_matrix(self,square_matrix: List[List[int]]) -> None:
        matrix_size = len(square_matrix) - 1
        for i in range(len(square_matrix) // 2):
            for j in range(i, matrix_size - i):
                # Perform a 4-way exchange. Note that A[~i] for i in [0, len(A) - 1]
                # is A[-(i + 1)].
                # when assigning variables in one line like this it ensures all are copied
                print("i,j",i,j,"~= -(i+1) ~i~j",~i,~j)
                (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j],
                square_matrix[j][~i]) = (square_matrix[~j][i], square_matrix[~i][~j],
                square_matrix[j][~i], square_matrix[i][j])

                # for more readability these are the assignments however when
                # done serially it will end in the wrong result

                # square_matrix[i][j] = square_matrix[-j][i]
                # square_matrix[-j][i]= square_matrix[-i][-j]
                # square_matrix[-i][-j] = square_matrix[j][-i]
                # square_matrix[j][-i] = square_matrix[i][j]
        print_matrix(square_matrix)
def print_matrix(A:List[List[int]])-> None:
    for i in range(len(A)):
        for j in range(len(A[i])):
            print(A[i][j], end=' ')
        print()


if __name__ =="__main__":
    mySolution = Solution()
    A = [
        [1,2,3,4],
        [5,6,7,8],
        [1,2,3,4],
        [5,6,7,8],
    ]
    mySolution.rotate_matrix(A)
