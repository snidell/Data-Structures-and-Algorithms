# 5.17 THE SUDOKU CHECKER PROBLEM
import math
class Solution:
    def is_valid_sudoku(self,partial_assignment: [[int]]) -> bool:
        # Return True i f subarray
        # partial_assignment[start_row:end_row][start_col:end_col] contains any
        #duplicates in {l, 2, ..., len(partial_assignment)}; otherwise return
        #False.
        def has_duplicates(block):
            print(block)
            block = list(filter(lambda x:x !=0, block))
            return len(block) !=len(set(block))
        n = len(partial_assignment)
        # [partial_assignment[i][j] for j in range(n)] loop through row
        # [partial_assignment[j][i] for j in range(n)] loop through column

        if any(has_duplicates([partial_assignment[i][j] for j in range(n)])
               or has_duplicates([partial_assignment[j][i] for j in range(n)])
               for i in range(n)):
                   return False

        region_size = int(math.sqrt(n))
        print("region size: ",region_size)
        return all(not has_duplicates([
            partial_assignment[a][b]
            for a in range(region_size*I,region_size*(I+1))
            for b in range(region_size*J,region_size*(J+1))
        ])for I in range(region_size) for J in range(region_size))



if __name__ =="__main__":
    mySolution = Solution()
    A = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,5,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    B = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,5,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,5,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]
    ]
    print(mySolution.is_valid_sudoku(A))
    print(mySolution.is_valid_sudoku(B))
