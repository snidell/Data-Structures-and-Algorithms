# 11.6 SEARCHING A 2D SORTED ARRAY
# Call a 2D array sorted if its rows and its columns are nondecreasing. See
# Figure 11.3 on the following page for an example of a 2D sorted array.
# Design an algorithm that takes a 2D sorted array and a number and checks
# whether that number appears in the array. For example, if the input is the
# 2D sorted array in Figure 11.3 on the next page, and the number is 7, your
# algorithm should return false; if the number is 8, your algorithm should
# return true.

# Hint: Can you eliminate a row or a column per comparison?

# an increasing array doesnt have repeating numbers. the next number is always
# larger than the previous ex: [1,2,3,4,5]
#  a non decreasing array could have multiples of the same number: [1,2,2,3,4,5]

from typing import List

class Solution:
    # O(m + n) time complexity.
    def matrix_search(self, A: List[List[int]], x: int) -> bool:
        row, col = 0 , len(A[0]) -1 # start from top right corner

        # keep  searchign while we are unclassified rows and columns
        while row < len(A) and col >= 0:
            if A[row][col] == x:
                return True
            elif A[row][col] < x:
                row += 1
            else:
                col -= 1
        return False


if __name__ =="__main__":
    mySolution = Solution()
    myMatrix =[
        [-1,2,4,4,6],
        [1,5,5,9,21],
        [3,6,6,9,22],
        [3,6,8,10,24],
        [6,8,9,12,25],
        [8,10,12,13,40]
    ]
    print("is 7 in the matrix? ",mySolution.matrix_search(myMatrix,7))
    print("is 8 in the matrix? ",mySolution.matrix_search(myMatrix,8))
