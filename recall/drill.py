# practice basic syntax
import collections
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from typing import List
class Solution:
    def __init__(self,myList1:List,myInt:int):
        self.myList = myList1
        self.myInt = myInt

    def solve_typing(self,list1:List, matrix:List[List[int]],myNum:int,myString:str)-> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [0] * rows
        dp2 = [0] * cols
        visited = [[0] * cols for _ in range (rows)]
        dp_2d = [[0] * rows for _ in range(10)]
        print(visited)
        print(matrix)

        # sorted containers

        mySorted = SortedList([[1,2],[-1,3]])
        print(mySorted.add([10,12]))

        def dfs(matrix,row,col,visited):
            print(row,col)
            if not(row >=0 and col >=0 and row< rows and col < cols and  matrix[row][col] == 1 and visited[row][col] ==0):
                return 0
            visited[row][col] = 1

            # go left right up down
            left = dfs(matrix,row - 1,col,visited)
            right = dfs(matrix,row + 1, col, visited)
            up = dfs(matrix,row,col - 1,visited)
            down = dfs(matrix,row,col + 1 , visited)


            return 1 + left+right+up+down
        area = 0
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 1 and visited[row][col] ==0:
                    area += dfs(matrix,row,col,visited)

        print("area of island is:",area)


        return True



if __name__ =="__main__":

    array1 = [1,2,3,4,5,6,7]
    array2 = [-1,4,9,10,13]
    mySolution = Solution(array2,10)
    matrix =[
              [0,1,1,1],
              [1,1,1,1],
              [0,1,1,1]
            ]
    print(mySolution.solve_typing(array1,matrix,1,"stuff"))
