# Given a rows x cols binary matrix filled with 0's and 1's, find the largest
# rectangle containing only 1's and return its area.

from typing import List

class Solution:
    # time complexity is O(n*m)
    # Space complexity is O(m)
    def maximalRectangle(self,matrix: List[List[int]])-> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0]*n
        right = [n]*n
        height = [0]*n

        max_area = 0

        for i in range(m):
            cur_left,cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] +=1
                else:
                    height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j],cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right go backwards
            for j in range(n - 1, -1, -1):
                if matrix[i][j] =='1':
                    right[j] = min(right[j],cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update area
            print("height: ",height)
            print("right: ",right)
            print("left: ",left)

            print()
            for j in range(n):
                print(max_area)
                max_area = max(max_area,(height[j] * (right[j] - left[j])))
        return max_area


if __name__ =="__main__":
    mySolution = Solution()
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    print(mySolution.maximalRectangle(matrix))
